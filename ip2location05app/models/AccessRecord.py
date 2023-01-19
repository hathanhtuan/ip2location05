from django.db import models

from ip2location05app.models.AccessGroup import AccessGroup
from ip2location05app.models.IPAddress import IPAddress


class AccessRecord(models.Model):
    ip = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    access_time = models.DateTimeField()
    access_group = models.ForeignKey(AccessGroup, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{} access at {}'.format(self.ip.address, self.access_time)
