from django.shortcuts import render
from django.views import View



class StatusesView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'statuses/index.html')


class CreateStatusesView(View):
    pass


class UpdateStatusesView(View):
    pass


class DeleteStatusesView(View):
    pass