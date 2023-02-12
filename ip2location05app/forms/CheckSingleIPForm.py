from django import forms

from ip2location05 import settings
from ip2location05app.forms import FormFactory
from ip2location05app.models.ApiConfiguration import ApiConfiguration


class CheckSingleIPForm(forms.Form):
    ip_address = FormFactory.ip_address_field(label='Enter IP address', required=True)
    api_configuration = FormFactory.model_choice_field_single(
        label='API Configuration',
        queryset=ApiConfiguration.objects.filter(
            api_config_type__contains=settings.DEFAULT_IP2LOCATION_TYPE_TEXT)
    )

