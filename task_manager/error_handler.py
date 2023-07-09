from django.shortcuts import render
from django.utils.translation import gettext as _


class ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code > 500:
            return render(request, 'error.html',
                          {'status': response.status_code,
                           'description': _('Internet server error')})

        if response.status_code > 400:
            return render(request, 'error.html',
                          {'status': response.status_code,
                           'description': _('Page not Found')})
        return response
