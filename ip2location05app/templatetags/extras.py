import json

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

keys_list = ['country_name', 'region_name', 'city_name', 'isp', 'domain', 'mobile_brand', 'usage_type']
keys_list_location = ['country_name', 'region_name', 'city_name']

@register.filter
def show_country(response_string):
    result = None
    try:
        result = json.loads(response_string)
    except:
        return response_string
    display_text = ''
    if result['response'] == 'OK':
        # if 'country_name' in result:
        #     display_text = display_text + result['country_name'] + ' - '
        # if 'region_name' in result:
        #     display_text = display_text + result['region_name'] + ' - '
        # if 'city_name' in result:
        #     display_text = display_text + result['city_name'] + ' - '
        for key in keys_list:
            if key in result:
                display_text = display_text + result[key] + ' - '
    return display_text

@register.filter
def show_location(response_string):
    result = None
    try:
        result = json.loads(response_string)
    except:
        return response_string
    display_text = ''
    if result['response'] == 'OK':
        # if 'country_name' in result:
        #     display_text = display_text + result['country_name'] + ' - '
        # if 'region_name' in result:
        #     display_text = display_text + result['region_name'] + ' - '
        # if 'city_name' in result:
        #     display_text = display_text + result['city_name'] + ' - '
        for key in keys_list_location:
            if key in result:
                display_text = display_text + result[key] + ' - '
    return display_text


@register.filter
def show_isp(response_string):
    result = None
    try:
        result = json.loads(response_string)
    except:
        return response_string
    display_text = ''
    if result['response'] == 'OK':
        if 'isp' in result:
            display_text = result['isp']

    return display_text


@register.filter
def show_all_dict(response_string):
    display_string = ''
    result = json.loads(response_string)
    if result:
        for key in result:
            display_string += '<p>{key}: <b>{value}</b></p>'.format(key=key, value=result[key])
    return mark_safe(display_string)


@register.filter
def show_per_page(current_page, request):
    per_page = request.GET.get('per_page', '')
    return_string = ''
    per_page_found = False
    for param, value in request.GET.items():
        if param != 'page' and param != 'per_page':
            return_string += '&{}={}'.format(param, value)
        if param == 'per_page':
            per_page_found = True
    if per_page_found:
        return return_string + '&page={}&per_page={}'.format(current_page, per_page)
    else:
        return return_string + '&page={}'.format(current_page)


@register.filter
def show_records_per_page_selection(total_record, request):
    per_page = request.GET.get('per_page', '')
    if per_page:
        per_page = int(per_page)
        if total_record == per_page:
            return 'selected'

        return ''

