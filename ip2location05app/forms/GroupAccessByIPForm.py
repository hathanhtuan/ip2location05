from django import forms

from ip2location05app.forms import FormFactory
from ip2location05app.models.ApiConfiguration import ApiConfiguration


class GroupAccessByIPForm(forms.Form):
    ip_list_file = FormFactory.file_field(label='Access Log', multiple=True)
