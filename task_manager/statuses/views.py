from django.urls import reverse_lazy
from task_manager.statuses.models import StatusModel
from task_manager.statuses.forms import StatusForm
from django.utils.translation import gettext as _
from task_manager.mixins import AppLoginMixin
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib import messages
from django.shortcuts import redirect


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

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = StatusModel.objects.get(id=status_id)
        if status.status_id.exists():
            messages.success(request, _("Can't delete status because it used"),
                             extra_tags="alert-danger")
        else:
            status.delete()
            messages.success(request, _('Status deleted successfully'),
                             extra_tags="alert-success")
        return redirect(reverse_lazy('status_list'))
