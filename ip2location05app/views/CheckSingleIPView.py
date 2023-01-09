from django.shortcuts import render
from django.urls import reverse_lazy

from ip2location05app.forms.CheckSingleIPForm import CheckSingleIPForm
from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.views.BaseIPCheckView import BaseIPCheckView


class CheckSingleIPView(BaseIPCheckView):
    form_class = CheckSingleIPForm
    template_name = 'check_single_ip.html'
    view_name = 'Check Single IP'
    success_url = reverse_lazy('single_ip_submit')

    def form_valid(self, form):
        ip_text = form.cleaned_data['ip_address']
        api_configuration = form.cleaned_data['api_configuration']
        if IPAddress.objects.filter(address=ip_text).exists():
            ip = IPAddress.objects.filter(address=ip_text).first()
        else:
            ip = IPAddress.objects.create(address=ip_text)

        result = self.check_ip(ip, api_configuration)
        context = form.get_context()
        context['result'] = result

        context = {
            'form': form,
            'result': result,
            'view_name': self.view_name
        }

        return render(self.request, 'check_single_ip.html', context)
