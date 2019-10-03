from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)

    # The additional attributes we wish to include.
    role = models.CharField(max_length = 100, blank = True)

# Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username