from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from task_manager.statuses.models import StatusModel
from task_manager.statuses.forms import StatusForm
from django.utils.translation import gettext as _
from django.contrib import messages


class StatusesView(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        statuses = StatusModel.objects.filter(user_id=user)
        return render(request, 'statuses/index.html', {'statuses': statuses})


class CreateStatusesView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm
        return render(request, 'statuses/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            user = request.user
            status.user_id = user
            status.save()
            messages.success(request, _('Status create successfully'),
                             extra_tags="alert-success")
            return redirect(reverse('statuses'))
        messages.success(request, _('Incorrect Form'),
                         extra_tags="alert-danger")
        return render(request, 'statuses/create.html', {'form': form})




class UpdateStatusesView(View):
    pass


class DeleteStatusesView(View):
    pass