from django.contrib.auth.models import User
from django.db import models

from ip2location05app.exceptions.CreatedByUserRequiredException import CreatedByUserRequiredException


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(app_label)s_%(class)s_created_by',
        editable=False)

    def save(self, *args, **kwargs):
        if self.created_by is None:
            raise CreatedByUserRequiredException
        super(CreatedByMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True
