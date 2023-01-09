from django import forms

from ip2location05app.forms import FormFactory
from ip2location05app.models.ApiConfiguration import ApiConfiguration


class CheckSingleIPForm(forms.Form):
    ip_address = FormFactory.ip_address_field(label='Enter IP address', required=True)
    api_configuration = FormFactory.model_choice_field_single(label='API Configuration',
                                                              queryset=ApiConfiguration.objects.all())

