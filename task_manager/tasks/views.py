from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django_filters.views import FilterView
from task_manager.mixins import AppLoginMixin
from task_manager.tasks.forms import TasksForm
from task_manager.tasks.models import TasksModel
from django.utils.translation import gettext as _
from task_manager.tasks.forms import FilterForm
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


class TaskListView(AppLoginMixin, FilterView, ListView):
    template_name = 'tasks/tasks.html'
    model = TasksModel
    filterset_class = FilterForm
    context_object_name = 'tasks'


class CreateTaskView(AppLoginMixin, CreateView):
    template_name = 'edit.html'
    model = TasksModel
    form_class = TasksForm
    success_url = reverse_lazy('task_list')
    success_message = _('Task create successfully')
    extra_context = {'title': _('Create task'), 'button': _('Create')}

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class UpdateTaskView(AppLoginMixin, UpdateView):
    template_name = 'edit.html'
    success_url = reverse_lazy('task_list')
    form_class = TasksForm
    model = TasksModel
    success_message = _('Task update successfully')
    extra_context = {'title': _('Update task'), 'button': _('Update')}


class DeleteTaskView(AppLoginMixin, DeleteView):
    template_name = 'delete.html'
    model = TasksModel
    success_url = reverse_lazy('task_list')
    success_message = _('Task deleted successfully')
    extra_context = {'title': _('Delete task')}


class TaskView(AppLoginMixin, View):
    template_name = 'tasks/task_view.html'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = TasksModel.objects.get(id=task_id)
        labels = task.labels.all()
        return render(request, self.template_name,
                      {'task': task, 'labels': labels})
