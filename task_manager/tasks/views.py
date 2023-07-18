from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from task_manager.utils import AppLoginMixin
from task_manager.tasks.forms import TasksForm
from task_manager.tasks.models import TasksModel
from django.utils.translation import gettext as _
from task_manager.tasks.forms import FilterForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class TaskListView(AppLoginMixin, ListView):
    template_name = 'tasks/tasks.html'
    model = TasksModel


class CreateTaskView(AppLoginMixin, CreateView):
    template_name = 'tasks/create.html'
    model = TasksModel
    form_class = TasksForm
    success_url = reverse_lazy('task_list')
    success_message = _('Task create successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class UpdateTaskView(AppLoginMixin, UpdateView):
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('task_list')
    form_class = TasksForm
    model = TasksModel
    success_message = _('Task update successfully')


class DeleteTaskView(AppLoginMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = TasksModel
    success_url = reverse_lazy('task_list')
    success_message = _('Task deleted successfully')

    # def get(self, request, *args, **kwargs):
    #     task_id = kwargs.get('pk')
    #     task = TasksModel.objects.get(id=task_id)
    #
    #     return render(request, self.template_name,
    #                   {'task': task})
    #
    # def post(self, request, *args, **kwargs):
    #     task_id = kwargs.get('pk')
    #     task = TasksModel.objects.get(id=task_id)
    #     if request.user.id == task.author_id:
    #         task.delete()
    #         messages.success(request, _('Task deleted successfully'),
    #                          extra_tags="alert-success")
    #         return redirect(reverse_lazy('task_list'))
    #
    #     messages.success(request, _('Only owner can remove the task'),
    #                      extra_tags="alert-danger")
    #     return redirect(reverse_lazy('task_list'))


class TaskView(AppLoginMixin, View):
    template_name = 'tasks/task_view.html'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = TasksModel.objects.get(id=task_id)
        labels = task.labels.all()
        return render(request, self.template_name,
                      {'task': task, 'labels': labels})
