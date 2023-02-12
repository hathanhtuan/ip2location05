from django import forms

from ip2location05 import settings
from ip2location05app.forms import FormFactory
from ip2location05app.forms.ExternalToolForm import ExternalToolForm
from ip2location05app.models.ApiConfiguration import ApiConfiguration


class ExternalToolFacebookSearchForm(ExternalToolForm):
    fb_id = FormFactory.char_field(label='Facebook ID', max_length=50, required=True)

    field_order = ['input', 'fb_id', 'api_configuration']



