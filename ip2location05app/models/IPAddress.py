import requests
from django.db import models

from ip2location05app.models.Config import Config


class IPAddress(models.Model):
    address = models.GenericIPAddressField()

    def __str__(self):
        return self.address

    def get_data_from_3rd_party(self):
        config = Config.objects.filter(is_active_config=True).first()
        if config:
            request_link = 'https://api.ip2location.com/v2/?ip={ip}&key={api}&format=json'\
                .format(ip=self.address, api=config.api_key)
            response = requests.get(request_link)
            print(response.content)
        else:
            raise Exception('No active config found')

