from django.db import models

from ip2location05app.models.ApiConfiguration import ApiConfiguration
from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.models.mixins.CreatedByMixin import CreatedByMixin
from ip2location05app.models.mixins.TimestampMixin import TimestampMixin


class Result(TimestampMixin, CreatedByMixin):
    response_string = models.CharField(max_length=1000)
    address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    api_configuration = models.ForeignKey(ApiConfiguration, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.response_string
