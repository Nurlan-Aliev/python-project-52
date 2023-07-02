from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from task_manager.utils import CheckAuthentication
from task_manager.tasks.forms import TasksForm
from task_manager.tasks.models import TasksModel
from django.utils.translation import gettext as _



class TaskListView(CheckAuthentication, View):
    template_name = 'tasks/tasks.html'

    def get(self, request, *args, **kwargs):
        tasks = TasksModel.objects.all()
        return render(request, self.template_name, {'tasks': tasks})


class CreateTaskView(CheckAuthentication, View):
    template_name = 'tasks/create.html'

    def get(self, request, *args, **kwargs):
        form = TasksForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            user = request.user
            task.author_id = user
            form.save()
            messages.success(request, _('Status create successfully'),
                             extra_tags="alert-success")
            return redirect(reverse_lazy('task_list'))
        messages.success(request, _('Incorrect Form'),
                         extra_tags="alert-danger")
        return render(request, self.template_name, {'form': form})


class UpdateTaskView(CheckAuthentication, View):
    pass


class DeleteTaskView(CheckAuthentication, View):
    pass


class TaskView(CheckAuthentication, View):
    pass
