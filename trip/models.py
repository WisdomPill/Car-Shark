from django.db import models


class Dummy(models.Model):
    semaphore = models.BooleanField(default=False)
    verb = models.CharField(blank=True, default='', max_length=32)
