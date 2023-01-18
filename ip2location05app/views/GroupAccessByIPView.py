import ipaddress
from abc import abstractmethod

from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render

from ip2location05app.forms.GroupAccessByIPForm import GroupAccessByIPForm
from ip2location05app.forms.UploadFileForm import UploadFileForm
from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.models.Result import Result
from ip2location05app.views.BaseIPCheckView import BaseIPCheckView
from datetime import datetime


class AccessGroup:
    ipaddress = None
    access_list = []

    def add_access(self, time):
        if isinstance(time, datetime):
            self.access_list.append(time)
        else:
            raise ValidationError('{} is not a valid time'.format(time))


class LogParser:

    @abstractmethod
    def parse_line(self, log_line):
        pass


class ZaloLogParser(LogParser):
    def parse_line(self, log_line, result_list=None):
        time_ip = log_line.split('\t')
        time = datetime.strptime(time_ip[0].split('.')[0], '%Y-%m-%d %H:%M:%S')
        ip = ipaddress.ip_address(time_ip[1])
        if result_list is None:
            result_list = {}
        if ip not in result_list:
            result_list[ip] = []
        result_list[ip].append(time)
        return result_list


class GroupAccessByIPView(BaseIPCheckView):
    form_class = UploadFileForm
    template_name = 'group_access_by_ip.html'
    view_name = 'Group Access By IP'

    def form_valid(self, form):
        files = self.request.FILES.getlist('ip_list_file')
        api_configuration = form.cleaned_data['api_configuration']
        ip_addresses = []
        file_input = None
        log_parser = ZaloLogParser()
        result_list = None
        result_list_with_api_check = {}
        with transaction.atomic():
            for f in files:
                file_name = str(f)
                for line in f:
                    line = line.rstrip().decode("utf-8")
                    result_list = log_parser.parse_line(line, result_list)
                    # {ip: [time1, time2, ...], ...}
            for result in result_list:
                if IPAddress.objects.filter(address=str(result)).exists():
                    ip = IPAddress.objects.filter(address=str(result)).first()
                else:
                    ip = IPAddress.objects.create(address=str(result))
                result_model = self.create_or_get_cached_result(ip, api_configuration, self.request.user)
                result_model.save()
                if ip not in result_list_with_api_check:
                    result_list_with_api_check[ip] = []

                result_model = self.check_ip(ip, api_configuration, self.request.user, result=result_model)
                result_model.save()
                result_list_with_api_check[ip].append({result: result_list.get(result)})
                result_list_with_api_check[ip].append(result_model)
                # {ip: [result, result_model], ...}

        context = form.get_context()

        context = {
            'form': form,
            'result_list': result_list_with_api_check,
            'view_name': self.view_name,
            'view': self
        }

        return render(self.request, 'group_access_by_ip.html', context)
