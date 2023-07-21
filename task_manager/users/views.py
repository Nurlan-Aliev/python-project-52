from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import (CreateView,
                                  DeleteView,
                                  UpdateView,
                                  ListView)
from django.utils.translation import gettext as _
from task_manager.users.forms import UserForm
from task_manager.mixins import UserPassMixin
from django.db.models import ProtectedError


class Users(ListView):
    template_name = 'users/users.html'
    model = User


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'edit.html'
    model = User
    success_url = reverse_lazy('login')
    success_message = _("User create successfully")
    extra_context = {'title': _('Sign Up'), 'button': _('Register')}


class UpdateUser(UserPassMixin, SuccessMessageMixin, UpdateView):
    template_name = 'edit.html'
    success_url = reverse_lazy('user_list')
    form_class = UserForm
    model = User
    success_message = _("User update successfully")
    extra_context = {'title': _('Update user'), 'button': _('Update')}


class DeleteUser(UserPassMixin, DeleteView):
    template_name = 'delete.html'
    model = User
    success_url = reverse_lazy('user_list')
    success_message = _("User deleted successfully")
    extra_context = {'title': _('Delete user')}

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(self.request, _("User was deleted successfully"))
        except ProtectedError:
            messages.add_message(
                request, messages.ERROR,
                _("Can't delete the user because it's used for the task"))
        return redirect(reverse_lazy('user_list'))
