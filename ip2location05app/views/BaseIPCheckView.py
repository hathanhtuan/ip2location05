
import ipaddress
import json
import logging
from datetime import datetime

import requests
from django.views.generic import FormView

from ip2location05 import settings
from ip2location05app.models.Result import Result
from ip2location05app.views.BaseView import BaseView

logger = logging.getLogger(__name__)


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
    def create_or_get_cached_result(ip, api_configuration, check_by_user):
        latest_result = Result.objects.filter(
            address__address=ip.address, api_configuration=api_configuration, checked=True
        ).order_by('-updated_at').first()
        use_cache = True
        result = None
        if latest_result is not None:
            days_delta = datetime.now().date() - latest_result.created_at.date()
            if days_delta.days >= settings.API_CACHE_PERIOD_DAYS:
                use_cache = False
        else:
            use_cache = False

        if use_cache:
            result = latest_result
        else:
            logger.info('create unchecked result to check ip {} with api {}'
                        .format(ip.address, api_configuration.get_api_link(ip.address))
                        )
            result = Result.objects.create(
                response_string='',
                address=ip,
                api_configuration=api_configuration,
                created_by=check_by_user,
                checked=False
            )
            result.save()
        return result

    @staticmethod
    def check_ip(ip, api_configuration, check_by_user, result=None):
        if result is None:
            result = BaseIPCheckView.create_or_get_cached_result(ip, api_configuration, check_by_user)
        if result.checked:
            return result
        else:
            response = requests.get(api_configuration.get_api_link(ip.address))
            logger.info('check ip {} with api {} - response {}'
                        .format(ip.address, api_configuration.get_api_link(ip.address), response.content)
                        )
            result.response_string = response.content.decode('utf-8')
            response_dict = json.loads(response.content)
            if response_dict['response'] == 'OK':
                result.checked = True
            else:
                result.checked = False
            result.save()
        return result


