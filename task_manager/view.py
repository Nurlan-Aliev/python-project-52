from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from task_manager.users.forms import LoginForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext as _


class HomePageViews(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            form = user.first_name
        else:
            form = 'World'

        return render(request, 'index.html', {'form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    redirect_field_name = '/'
    authentication_form = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.authentication_form})

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        if request.user.is_authenticated:
            messages.success(request, _('You have successfully logged in'), extra_tags="alert-success")
            return redirect(reverse('home_page'))
        messages.error(request, _('Incorrect Form'), extra_tags="alert-danger")
        return render(request, self.template_name, {'form': self.authentication_form})


class Logout(LogoutView):
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        messages.info(request, _("You have successfully logged out"), extra_tags="alert-info")
        return redirect(self.next_page)
