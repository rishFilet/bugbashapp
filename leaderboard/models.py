from django.db import models


# Create your models here.
class Leaderboard(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    product = models.CharField(max_length = 100)
    total = models.CharField(max_length = 100)
