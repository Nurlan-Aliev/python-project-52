from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from task_manager.utils import CheckAuthentication
from task_manager.tasks.forms import TasksForm
from task_manager.tasks.models import TasksModel
from django.utils.translation import gettext as _
from django.views.generic import DeleteView


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
    template_name = 'tasks/update.html'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = TasksModel.objects.get(id=task_id)
        form = TasksForm(instance=task)
        return render(request, self.template_name,
                      {'form': form, 'task_id': task_id})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = TasksModel.objects.get(id=task_id)
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, _('Status update successfully'),
                             extra_tags="alert-success")
            return redirect(reverse_lazy('task_list'))
        messages.success(request, _('Incorrect Form'),
                         extra_tags="alert-danger")
        return render(request, self.template_name, {'form': form})


class DeleteTaskView(CheckAuthentication, DeleteView):
    template_name = 'tasks/delete.html'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = TasksModel.objects.get(id=task_id)
        print()

        return render(request, self.template_name,
                      {'task': task})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = TasksModel.objects.get(id=task_id)
        if request.user.id == task.author_id:
            task.delete()
            messages.success(request, _('Status deleted successfully'),
                             extra_tags="alert-success")
            return redirect(reverse_lazy('task_list'))

        messages.success(request, _('Only owner can remove the task'),
                         extra_tags="alert-danger")
        return redirect(reverse_lazy('task_list'))


class TaskView(CheckAuthentication, View):
    template_name = 'tasks/task_view.html'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = TasksModel.objects.get(id=task_id)
        labels = task.labels.all()
        print(labels)
        return render(request, self.template_name,
                      {'task': task, 'labels': labels})
