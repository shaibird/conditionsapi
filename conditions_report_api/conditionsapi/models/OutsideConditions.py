from django.db import models

class OutsideConditions(models.Model):
    condition = models.CharField(max_length=150)