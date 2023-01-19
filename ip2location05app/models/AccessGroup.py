from django.db import models

from ip2location05app.models.FileInput import FileInput
from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.models.Result import Result


class AccessGroup(models.Model):
    ip = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    file_input = models.ForeignKey(FileInput, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        if self.ip is not None:
            return self.ip.address
        return 'Access Group {}'.format(self.pk)
