from django.db import models


# Create your models here.
class Leaderboard(models.Model):
    rank = models.PositiveIntegerField(default = 0, blank = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    Camera = models.PositiveIntegerField(default = 0, blank = True)
    Tstat = models.PositiveIntegerField(default = 0, blank = True)
    Sensors = models.PositiveIntegerField(default = 0, blank = True)
    Ls = models.PositiveIntegerField(default = 0, blank = True)
    Eco_plus = models.PositiveIntegerField(default = 0, blank = True)
    Iris = models.PositiveIntegerField(default = 0, blank = True)
    total = models.PositiveIntegerField(default = 0, blank = True)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields = ['first_name', 'last_name'], name = 'first last
    # name')
    #     ]

    def __str__(self):
        return self.first_name
