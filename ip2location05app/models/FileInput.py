from django.db import models

from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.models.mixins.TimestampMixin import TimestampMixin


class FileInput(TimestampMixin):
    file_name = models.CharField(max_length=256)
    addresses = models.ManyToManyField(IPAddress)
