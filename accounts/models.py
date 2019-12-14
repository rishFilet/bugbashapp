import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(_('email address'), unique=True)
	role = models.CharField(max_length=100, blank=True, default="Bug Catcher")
	user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email
