from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView
from task_manager.statuses.models import StatusModel
from task_manager.statuses.forms import StatusForm
from django.utils.translation import gettext as _
from django.contrib import messages
from task_manager.utils import CheckAuthentication


class StatusesView(CheckAuthentication, View):
    template_name = 'statuses/index.html'

    def get(self, request, *args, **kwargs):
        statuses = StatusModel.objects.all()
        return render(request, self.template_name, {'statuses': statuses})


class CreateStatusesView(CheckAuthentication, View):
    template_name = 'statuses/create.html'

    def get(self, request, *args, **kwargs):
        form = StatusForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, _('Status create successfully'),
                             extra_tags="alert-success")
            return redirect(reverse_lazy('status_list'))

        messages.success(request, _('Incorrect Form'),
                         extra_tags="alert-danger")
        return render(request, self.template_name, {'form': form})


class UpdateStatusesView(CheckAuthentication, View):
    template_name = 'statuses/update.html'

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = StatusModel.objects.get(id=status_id)
        form = StatusForm(instance=status)

        return render(request, self.template_name,
                      {'form': form, 'status_id': status_id})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = StatusModel.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)

        if form.is_valid():
            form.save()
            messages.success(request, _('Status update successfully'),
                             extra_tags="alert-success")
            return redirect(reverse_lazy('status_list'))

        messages.success(request, _('Incorrect Form'),
                         extra_tags="alert-danger")
        return render(request, self.template_name, {'form': form})


class DeleteStatusesView(CheckAuthentication, DeleteView):
    template_name = 'statuses/delete.html'

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = StatusModel.objects.get(id=status_id)

        return render(request, self.template_name, {
            'status': status})

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
