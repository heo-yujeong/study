from django.db import models

# Create your models here.
class Todos(models.Model):
    todo = models.TextField()