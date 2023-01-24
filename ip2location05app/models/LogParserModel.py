from django.db import models


class LogParserModel(models.Model):
    class_name = models.CharField(max_length=20)
    module_path = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.class_name
