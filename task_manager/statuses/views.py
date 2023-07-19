from django.urls import reverse_lazy
from task_manager.statuses.models import StatusModel
from task_manager.statuses.forms import StatusForm
from django.utils.translation import gettext as _
from task_manager.utils import AppLoginMixin
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


class StatusesView(AppLoginMixin, ListView):
    template_name = 'statuses/index.html'
    model = StatusModel


class CreateStatusesView(AppLoginMixin, CreateView):
    template_name = 'edit.html'
    form_class = StatusForm
    model = StatusModel
    success_url = reverse_lazy('status_list')
    success_message = _("Status create successfully")
    extra_context = {'title': _('Create status'), 'button': _('Create')}


class UpdateStatusesView(AppLoginMixin, UpdateView):
    template_name = 'edit.html'
    form_class = StatusForm
    model = StatusModel
    success_url = reverse_lazy('status_list')
    success_message = _("Status update successfully")
    extra_context = {'title': _('Update status'), 'button': _('Update')}


class DeleteStatusesView(AppLoginMixin, DeleteView):
    template_name = 'delete.html'
    model = StatusModel
    success_url = reverse_lazy('status_list')
    success_message = _('Status deleted successfully')
    extra_context = {'title': _('Delete status')}
