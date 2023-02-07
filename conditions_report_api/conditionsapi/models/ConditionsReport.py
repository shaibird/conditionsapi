from django.db import models
from django.contrib.auth.models import User


class ConditionsReport(models.Model):
    description = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crag = models.ForeignKey("Crags", on_delete=models.CASCADE)
    goals = models.ForeignKey("Goals", on_delete=models.CASCADE)
    outsideconditions = models.ForeignKey("outsideconditions", on_delete=models.CASCADE, related_name="conditions")
    rock_conditions = models.ForeignKey("RockConditions", on_delete=models.CASCADE)
    time_of_day = models.ForeignKey("TimeOfDay", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)