from django import forms

from ip2location05 import settings
from ip2location05app.forms import FormFactory
from ip2location05app.models.ApiConfiguration import ApiConfiguration


class ExternalToolForm(forms.Form):
    input = FormFactory.char_field(label='Search', max_length=50, required=True)
    api_configuration = FormFactory.model_choice_field_multiple_checkbox(
        label='Choose tool(s)',
        queryset=None
    )

