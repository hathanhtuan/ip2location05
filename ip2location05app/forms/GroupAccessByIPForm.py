from django import forms

from ip2location05app.forms import FormFactory
from ip2location05app.models.ApiConfiguration import ApiConfiguration
from ip2location05app.models.LogParserModel import LogParserModel


class GroupAccessByIPForm(forms.Form):
    ip_list_file = FormFactory.file_field(label='Access Log', multiple=True)
    api_configuration = FormFactory.model_choice_field_single(label='API Configuration',
                                                              queryset=ApiConfiguration.objects.all())
    log_parser = FormFactory.model_choice_field_single(
        label='Log Parser', queryset=LogParserModel.objects.filter(is_active=True)
    )
