from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account(AbstractUser):
    """
    Account model for Authentication and Authorization
    """
    phone_number = models.CharField(max_length=128, default='')

