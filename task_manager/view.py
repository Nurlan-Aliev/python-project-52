from django.core.mail import message
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from task_manager.users.forms import LoginForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


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
    message
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.authentication_form})

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return redirect(reverse('home_page'))


class Logout(LogoutView):
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, "Three credits remain in your account.")
        return redirect(self.next_page)
