from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(max_length=100,unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username","first_name","last_name","password"]