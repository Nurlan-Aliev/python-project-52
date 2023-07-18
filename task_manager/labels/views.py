from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from task_manager.utils import AppLoginMixin
from django.views import View
from task_manager.labels.models import LabelModel
from task_manager.labels.forms import LabelForms
from django.contrib import messages
from django.utils.translation import gettext as _


class LabelView(AppLoginMixin, View):
    template_name = 'labels/labels.html'

    def get(self, request, *args, **kwargs):
        labels = LabelModel.objects.all()
        return render(request, self.template_name, {'labels': labels})


class CreateLabel(AppLoginMixin, View):
    template_name = 'labels/create.html'

    def get(self, request, *args, **kwargs):
        form = LabelForms
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LabelForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Label create successfully'),
                             extra_tags="alert-success")
            return redirect(reverse_lazy('label_list'))
        messages.success(request, _('Incorrect Form'),
                         extra_tags="alert-danger")
        return render(request, self.template_name, {'form': form})


class UpdateLabel(AppLoginMixin, View):
    template_name = 'labels/update.html'

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = LabelModel.objects.get(id=label_id)
        form = LabelForms(instance=label)
        return render(request, self.template_name,
                      {'form': form, 'label_id': label_id})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = LabelModel.objects.get(id=label_id)
        form = LabelForms(request.POST, instance=label)
        if form.is_valid():
            messages.success(request, _('Label update successfully'),
                             extra_tags="alert-success")
            form.save()
            return redirect(reverse_lazy('label_list'))
        messages.success(request, _('Incorrect Form'),
                         extra_tags="alert-danger")
        return render(request, self.template_name,
                      {'form': form, 'label_id': label_id})


class DeleteLabel(AppLoginMixin, DeleteView):
    template_name = 'labels/delete.html'

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = LabelModel.objects.get(id=label_id)
        return render(request, self.template_name, {'label': label})

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
