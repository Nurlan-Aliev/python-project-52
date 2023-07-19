from django.urls import reverse_lazy
from task_manager.utils import AppLoginMixin
from task_manager.labels.models import LabelModel
from task_manager.labels.forms import LabelForms
from django.utils.translation import gettext as _
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


class LabelView(AppLoginMixin, ListView):
    template_name = 'labels/labels.html'
    model = LabelModel


class CreateLabel(AppLoginMixin, CreateView):
    template_name = 'edit.html'
    form_class = LabelForms
    model = LabelModel
    success_message = 'Label create successfully'
    success_url = reverse_lazy('label_list')
    extra_context = {'title': _('Create label'), 'button': _('Create')}


class UpdateLabel(AppLoginMixin, UpdateView):
    template_name = 'edit.html'
    model = LabelModel
    form_class = LabelForms
    success_url = reverse_lazy('label_list')
    success_message = _('Label deleted successfully')
    extra_context = {'title': _('Update label'), 'button': _('Update')}


class DeleteLabel(AppLoginMixin, DeleteView):
    template_name = 'delete.html'
    model = LabelModel
    success_url = reverse_lazy('label_list')
    success_message = _('Label deleted successfully')
    extra_context = {'title': _('Delete label')}
