from django.db import models

from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.models.Result import Result
from ip2location05app.models.mixins.CreatedByMixin import CreatedByMixin
from ip2location05app.models.mixins.TimestampMixin import TimestampMixin


class FileInput(TimestampMixin, CreatedByMixin):
    file_name = models.CharField(max_length=256)
    addresses = models.ManyToManyField(IPAddress)
    results = models.ManyToManyField(Result)

    def __str__(self):
        return self.file_name
    
