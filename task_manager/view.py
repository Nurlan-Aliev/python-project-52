from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _


class HomePageViews(View):

    def get(self, request):
        context = {
            'Task_Manager': _('Task Manager'),
        }
        return render(request, 'index.html', context)
