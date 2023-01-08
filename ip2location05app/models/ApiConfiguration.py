from django.db import models

from ip2location05app.models.Api3rdParty import Api3rdParty
from ip2location05app.models.mixins.TimestampMixin import TimestampMixin


class ApiConfiguration(TimestampMixin):
    description = models.CharField(max_length=50)
    params = models.CharField(max_length=200)
    api_3rd_party = models.ForeignKey(Api3rdParty, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def get_api_link(self, ip):
        return self.api_3rd_party.api_source + self.params.format(api_key=self.api_3rd_party.api_key, ip=ip)

