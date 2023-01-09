import ipaddress

import requests
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from ip2location05app.forms.UploadFileForm import UploadFileForm
from ip2location05app.models.FileInput import FileInput
from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.models.Result import Result
from ip2location05app.views.BaseIPCheckView import BaseIPCheckView
from ip2location05app.views.BaseView import BaseView


class FileSubmitView(BaseIPCheckView):
    form_class = UploadFileForm
    template_name = 'file_submit.html'
    view_name = 'Submit file contains list IPs'

    # def get_initial(self):
    #     initial = super(FileSubmitView, self).get_initial()
    #     initial['api_configuration'] = ApiConfiguration.objects.all()

    def form_valid(self, form):
        files = self.request.FILES.getlist('ip_list_file')
        ip_addresses = []
        file_input = None
        with transaction.atomic():
            for f in files:
                file_name = str(f)
                file_input = FileInput.objects.create(file_name=file_name)
                file_input.save()
                for line in f:
                    line = line.rstrip().decode("utf-8")
                    ipt = str(line)
                    if not self.is_valid_ipaddress(ipt):
                        raise ValidationError('IP Address is not valid {}'.format(ipt))
                    if IPAddress.objects.filter(address=ipt).exists():
                        ip = IPAddress.objects.filter(address=ipt).first()
                    else:
                        ip = IPAddress.objects.create(address=ipt)
                    ip.save()
                    ip_addresses.append(ip)
                    file_input.addresses.add(ip)
                    file_input.save()
        api_configuration = form.cleaned_data['api_configuration']
        if file_input and api_configuration:
            for ip in ip_addresses:
                self.check_ip(ip, api_configuration)
            return redirect(reverse('result_list') + '?file_id=' + str(file_input.pk))
        else:
            return redirect('result_list')
