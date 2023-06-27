from django.shortcuts import render
from django.views import View
from task_manager.statuses.models import StatusModel


class StatusesView(View):

    def get(self, request, *args, **kwargs):
        statuses = StatusModel.objects.all()
        return render(request, 'statuses/index.html', {'statuses': statuses})


class CreateStatusesView(View):
    pass


class UpdateStatusesView(View):
    pass


class DeleteStatusesView(View):
    pass