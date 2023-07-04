from django.db import models


class StatusModel(models.Model):

    name = models.CharField(
        max_length=100, unique=True,
        error_messages={'unique': "Это имя уже существует."})

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
