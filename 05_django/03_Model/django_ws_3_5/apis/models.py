from django.db import models
from django.core.validators import URLValidator
from django.core.validators import MinLengthValidator


class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(validators=[URLValidator(60), MinLengthValidator(15)])
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
