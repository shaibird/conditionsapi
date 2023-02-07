from django.db import models

class Goals(models.Model):
    goal = models.CharField(max_length=50)