from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.mixins import AppLoginMixin
from task_manager.labels.models import LabelModel
from task_manager.labels.forms import LabelForms
from django.utils.translation import gettext as _
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.messages.views import SuccessMessageMixin


class LabelView(AppLoginMixin, ListView):
    template_name = 'labels/labels.html'
    model = LabelModel


class CreateLabel(AppLoginMixin, CreateView):
    template_name = 'edit.html'
    form_class = LabelForms
    model = LabelModel
    success_message = _('Label create successfully')
    success_url = reverse_lazy('label_list')
    extra_context = {'title': _('Create label'), 'button': _('Create')}


class UpdateLabel(AppLoginMixin, SuccessMessageMixin, UpdateView):
    template_name = 'edit.html'
    model = LabelModel
    form_class = LabelForms
    success_url = reverse_lazy('label_list')
    success_message = _('Label update successfully')
    extra_context = {'title': _('Update label'), 'button': _('Update')}


class DeleteLabel(AppLoginMixin, DeleteView):
    template_name = 'delete.html'
    model = LabelModel
    success_url = reverse_lazy('label_list')
    success_message = _('Label deleted successfully')
    extra_context = {'title': _('Delete label')}

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = LabelModel.objects.get(id=label_id)

        if label.tasksmodel_set.exists():
            messages.success(request, _("Can't delete label because it used"),
                             extra_tags="alert-danger")

        else:
            label.delete()
            messages.success(request, _('Label deleted successfully'),
                             extra_tags="alert-success")

        return redirect(reverse_lazy('label_list'))
