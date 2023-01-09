import ipaddress

import requests
from django.views.generic import FormView

from ip2location05app.models.Result import Result
from ip2location05app.views.BaseView import BaseView


class BaseIPCheckView(BaseView, FormView):
    @staticmethod
    def is_valid_ipaddress(sample_str):
        """ Returns True if given string is a
            valid IP Address, else returns False"""
        result = True
        try:
            ipaddress.ip_network(sample_str)
        except:
            result = False
        return result

    @staticmethod
    def check_ip(ip, api_configuration, check_by_user):
        response = requests.get(api_configuration.get_api_link(ip.address))
        result = Result.objects.create(
            response_string=response.content.decode('utf-8'),
            address=ip,
            api_configuration=api_configuration,
            created_by=check_by_user
        )
        result.save()
        return result
