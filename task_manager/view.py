from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from task_manager.users.forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext as _


class HomePageViews(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            form = user.first_name
        else:
            form = 'World'

        return render(request, self.template_name, {'form': form})


class LoginUser(LoginView):
    template_name = 'login.html'
    redirect_field_name = reverse_lazy('home_page')
    authentication_form = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {'form': self.authentication_form})

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        if request.user.is_authenticated:
            messages.success(request, _('You are logged in'),
                             extra_tags="alert-success")
            return redirect(self.redirect_field_name)

        messages.error(request, _('Incorrect Form'),
                       extra_tags="alert-danger")
        return render(request, self.template_name,
                      {'form': self.authentication_form})


class Logout(LogoutView):
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        messages.info(request, _("You are logged out"),
                      extra_tags="alert-info")
        return redirect(self.next_page)
