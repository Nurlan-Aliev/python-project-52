from django.db import models
from task_manager.statuses.models import StatusModel
from django.contrib.auth.models import User


class TasksModel(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status_id = models.ForeignKey(StatusModel, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    executor_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor', null=True)

    def __str__(self):
        return self.name
