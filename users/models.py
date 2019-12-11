from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(_('email address'), unique=True, default="Some Crap")
	role = models.CharField(max_length=100, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email





# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# # Create your models here.
# class CustomUser(AbstractUser):
#     role = models.CharField(max_length = 100, blank = True)
#     uid = models.CharField(max_length = 500, blank = True)
#
#     def __str__(self):
#         return self.email
