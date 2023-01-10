import json

from django import template

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
