from django.db import models


# Create your models here.
class Leaderboard(models.Model):
    rank = models.PositiveIntegerField(default = 0, blank = True, primary_key = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    iOS = models.PositiveIntegerField(default = 0, blank = True)
    Android = models.PositiveIntegerField(default = 0, blank = True)
    TSTAT = models.PositiveIntegerField(default = 0, blank = True)
    CAMERA = models.PositiveIntegerField(default = 0, blank = True)
    SENSORS = models.PositiveIntegerField(default = 0, blank = True)
    SWITCH = models.PositiveIntegerField(default = 0, blank = True)
    ECO_PLUS = models.PositiveIntegerField(default = 0, blank = True)
    total = models.PositiveIntegerField(default = 0, blank = True)
