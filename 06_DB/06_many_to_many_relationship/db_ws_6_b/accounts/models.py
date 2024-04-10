from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    subscription = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, related_name='subscriber')
