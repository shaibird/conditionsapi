from django.db import models

class RockConditions(models.Model):
    condition = models.CharField(max_length=150)