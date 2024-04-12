from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()

class Query(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    keyword = models.TextField()