from django.db import models
from task_manager.statuses.models import StatusModel
from django.contrib.auth.models import User
from task_manager.labels.models import LabelModel


class TasksModel(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(StatusModel, on_delete=models.PROTECT, related_name='status_id')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_id')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor_id', null=True)
    labels = models.ManyToManyField(LabelModel)

    def __str__(self):
        return self.name
