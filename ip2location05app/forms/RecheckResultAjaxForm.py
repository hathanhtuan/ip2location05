from django.forms import forms

from ip2location05app.forms import FormFactory


class RecheckResultAjaxForm(forms.Form):
    result_id = FormFactory.int_field(label='result_id')
