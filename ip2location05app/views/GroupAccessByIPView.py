import ipaddress
from abc import abstractmethod

from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse

from ip2location05app.forms.GroupAccessByIPForm import GroupAccessByIPForm
from ip2location05app.forms.UploadFileForm import UploadFileForm
from ip2location05app.models.AccessGroup import AccessGroup
from ip2location05app.models.AccessRecord import AccessRecord
from ip2location05app.models.FileInput import FileInput
from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.models.Result import Result
from ip2location05app.views.BaseIPCheckView import BaseIPCheckView
from datetime import datetime


# class AccessGroup:
#     ipaddress = None
#     access_list = []
#
#     def add_access(self, time):
#         if isinstance(time, datetime):
#             self.access_list.append(time)
#         else:
#             raise ValidationError('{} is not a valid time'.format(time))


class LogParser:

    @abstractmethod
    def parse_line(self, log_line):
        pass


class ZaloLogParser(LogParser):
    def parse_line(self, log_line):
        time_ip = log_line.split('\t')
        time = datetime.strptime(time_ip[0].split('.')[0], '%Y-%m-%d %H:%M:%S')
        ip = ipaddress.ip_address(time_ip[1])
        ip_model = None
        if IPAddress.objects.filter(address=str(ip)).exists():
            ip_model = IPAddress.objects.filter(address=str(ip)).first()
        else:
            ip_model = IPAddress.objects.create(address=str(ip))

        access_record = AccessRecord.objects.create(ip=ip_model, access_time=time, access_group=None)
        return access_record


class GroupAccessByIPView(BaseIPCheckView):
    form_class = UploadFileForm
    template_name = 'group_access_by_ip.html'
    view_name = 'Group Access By IP'

    def form_valid(self, form):
        files = self.request.FILES.getlist('ip_list_file')
        file_input = None
        api_configuration = form.cleaned_data['api_configuration']
        log_parser = ZaloLogParser()
        access_group_list = {}
        with transaction.atomic():
            for f in files:
                file_name = str(f)
                file_input = FileInput.objects.create(file_name=file_name, created_by=self.request.user)
                file_input.save()
                for line in f:
                    line = line.rstrip().decode("utf-8")
                    access_record = log_parser.parse_line(line)
                    if access_record.ip in access_group_list:
                        access_record.access_group = access_group_list[access_record.ip]
                        access_record.save()
                    else:
                        access_group = AccessGroup.objects.create(ip=access_record.ip, file_input=file_input)
                        access_group.save()
                        result = self.create_or_get_cached_result(
                            access_record.ip, api_configuration, self.request.user
                        )
                        file_input.results.add(result)
                        file_input.addresses.add(access_record.ip)
                        file_input.save()
                        result.save()
                        access_group.result = result
                        access_group.save()
                        access_group_list[access_record.ip] = access_group
                        access_record.access_group = access_group
                        access_record.save()

            for ip, ag in access_group_list.items():
                if not ag.result.checked:
                    ag.result = self.check_ip(ag.ip, api_configuration, self.request.user, result=ag.result)
                    ag.result.save()

        # return render(self.request, 'group_access_by_ip.html', context)
        return redirect(reverse('group_access_result') + '?file_id=' + str(file_input.pk))
