from django.db import models
from django.contrib.auth.models import User


class StatusModel(models.Model):

    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
