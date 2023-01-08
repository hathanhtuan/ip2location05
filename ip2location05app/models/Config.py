from django.db import models
from django.db.models import Model

from ip2location05app.models.mixins.TimestampMixin import TimestampMixin


class Config(TimestampMixin):
    api_key = models.CharField(max_length=20)
    is_active_config = models.BooleanField(default=False)
