from django.db import models

# Create your models here.
class Login:
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length=200)