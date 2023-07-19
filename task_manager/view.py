from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from task_manager.users.forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin


class HomePageViews(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            full_name = f"{ user.first_name } { user.last_name }"
        else:
            full_name = _('World')

        return render(request, self.template_name, {'full_name': full_name})


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home_page')
    authentication_form = LoginForm
    success_message = _('You are logged in')
    extra_context = {'title': _('login'), 'button': _('Sign in')}



class Logout(LogoutView, SuccessMessageMixin):
    next_page = reverse_lazy('home_page')
    success_message = _('You are logged out')
