from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # user.followings.all() => 내가 참조하고 있는 유저들
    # user.followers.all() => 나를 참조하고 있는 유저들