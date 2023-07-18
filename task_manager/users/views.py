from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.utils.translation import gettext as _
from task_manager.users.forms import UserForm
from task_manager.utils import AppLoginMixin


class Users(ListView):
    template_name = 'users/users.html'
    model = User


class CreateUser(CreateView, SuccessMessageMixin):
    form_class = UserForm
    template_name = 'users/create.html'
    model = User
    success_url = reverse_lazy('login')
    success_message = _("User create successfully")


class UpdateUser(AppLoginMixin, UpdateView, SuccessMessageMixin):
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_list')
    form_class = UserForm
    model = User
    success_message = _("User create successfully")


class DeleteUser(AppLoginMixin, SuccessMessageMixin, DeleteView, ):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('user_list')
    success_message = _("User deleted successfully")
