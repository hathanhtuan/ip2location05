import json

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def show_country(response_string):
    result = json.loads(response_string)
    display_text = ''
    if result['response'] == 'OK':
        if 'country_name' in result:
            display_text = display_text + result['country_name'] + ' - '
        if 'region_name' in result:
            display_text = display_text + result['region_name'] + ' - '
        if 'city_name' in result:
            display_text = display_text + result['city_name'] + ' - '
    return display_text


@register.filter
def show_all_dict(response_string):
    display_string = ''
    result = json.loads(response_string)
    if result:
        for key in result:
            display_string += '<p>{key}: <b>{value}</b></p>'.format(key=key, value=result[key])
    return mark_safe(display_string)

