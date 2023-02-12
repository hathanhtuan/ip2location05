from django.db import models


class Api3rdParty(models.Model):
    api_key = models.CharField(max_length=200, null=True, blank=True)
    api_source = models.CharField(max_length=200, null=True, blank=True)
    api_name = models.CharField(max_length=50)

    def __str__(self):
        return self.api_name
