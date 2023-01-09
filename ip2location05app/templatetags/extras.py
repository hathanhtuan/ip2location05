import json

from django import template

register = template.Library()


@register.filter
def show_country(response_string):
    result = json.loads(response_string)
    return result['country_name']
