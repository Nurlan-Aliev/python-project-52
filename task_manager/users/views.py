from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.utils.translation import gettext as _
from task_manager.users.forms import UsersForm
from task_manager.utils import CheckAuthentication
from pathlib import Path



class Users(View):
    template_name = 'users/users.html'

    def get(self, request):
        print(Path(__file__).resolve().parent.parent)
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})


class CreateUser(CreateView):
    form_class = UserCreationForm
    template_name = 'users/create.html'

    def get(self, request, *args, **kwargs):
        form = UsersForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('User create successfully'),
                             extra_tags="alert-success")
            return redirect(reverse('login'))

        messages.error(request, _('Incorrect Form'),
                       extra_tags="alert-danger")
        return render(request, self.template_name, {'form': form})


class UpdateUser(CheckAuthentication, View):
    template_name = 'users/update.html'

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.id != kwargs.get('pk'):
            messages.error(request, _(
                'You do not have rights to change another user.'),
                extra_tags="alert-danger")
            return redirect(reverse('user_list'))

        form = UsersForm(instance=user)
        return render(request, self.template_name,
                      {'form': form, 'user_id': user.id})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = UsersForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, _('User changed successfully'),
                             extra_tags="alert-success")
            return redirect(reverse('user_list'))

        messages.error(request, _('Incorrect Form'),
                       extra_tags="alert-danger")
        return render(request, 'users/update.html',
                      {'form': form, 'user_id': user.id})


class DeleteUser(CheckAuthentication, DeleteView):
    template_name = 'users/delete.html'

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.id != kwargs.get('pk'):
            messages.error(request, _(
                'You do not have rights to change another user.'),
                extra_tags="alert-danger")
            return redirect(reverse('user_list'))

        return render(request, self.template_name,
                      {'user': user, 'user_id': user.id})

    def post(self, request, *args, **kwargs):
        user = request.user

        if user.author_id.exists() or user.executor_id.exists():
            messages.success(request, _("Can't delete user because it used"),
                             extra_tags="alert-danger")

        else:
            messages.success(request, _('User deleted successfully'),
                             extra_tags="alert-success")

            user.delete()

        return redirect(reverse('user_list'))
