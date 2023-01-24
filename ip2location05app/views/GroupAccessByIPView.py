import importlib
import ipaddress
import logging
from abc import abstractmethod
from datetime import datetime

from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse

from ip2location05app.forms.GroupAccessByIPForm import GroupAccessByIPForm
from ip2location05app.models.AccessGroup import AccessGroup
from ip2location05app.models.AccessRecord import AccessRecord
from ip2location05app.models.FileInput import FileInput
from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.views.BaseIPCheckView import BaseIPCheckView

logger = logging.getLogger(__name__)

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


def str_to_class(module_name, class_name):
    """Return a class instance from a string reference"""
    try:
        module_ = importlib.import_module(module_name)
        try:
            class_ = getattr(module_, class_name)
        except AttributeError:
            logger.error('Class does not exist')
    except ImportError:
        logger.error('Module does not exist')
    return class_ or None


class GroupAccessByIPView(BaseIPCheckView):
    form_class = GroupAccessByIPForm
    template_name = 'group_access_by_ip.html'
    view_name = 'Group Access By IP'

    def form_valid(self, form):
        files = self.request.FILES.getlist('ip_list_file')
        file_input = None
        api_configuration = form.cleaned_data['api_configuration']
        log_parser_model = form.cleaned_data['log_parser']
        log_parser = None
        class_ = str_to_class(log_parser_model.module_path, log_parser_model.class_name)
        if class_:
            log_parser = class_()
        else:
            raise ImportError('Class not found')
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
        return redirect(reverse('group_access_result') + '?file=' + str(file_input.pk))
