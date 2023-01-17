import ipaddress

from django.db import models

from ip2location05app.models.ISP import ISP


class IPNetwork(models.Model):
    ip_network = models.CharField(max_length=50)
    isp = models.ForeignKey(ISP, on_delete=models.CASCADE)
    is_mobile_network = models.BooleanField(default=False)

    def __str__(self):
        return self.ip_network

    def full_clean(self, exclude=None, validate_unique=True, validate_constraints=True):
        ip_network = ipaddress.ip_network(self.ip_network)
        return super().full_clean(exclude, validate_unique, validate_constraints)
