from django.db import models

class Crags(models.Model):
    cragName = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=150)
