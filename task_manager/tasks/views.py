from django.shortcuts import render
from django.views import View
from task_manager.utils import CheckAuthentication


class TaskView(CheckAuthentication, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/tasks.html')


class CreateTaskView(CheckAuthentication, View):
    pass


class UpdateTaskView(CheckAuthentication, View):
    pass


class DeleteTaskView(CheckAuthentication, View):
    pass
