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


class Users(View):

    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'users/users.html', context)


class CreateUser(CreateView):
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = UsersForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('User create successfully'),
                             extra_tags="alert-success")
            return redirect(reverse('login'))

        messages.error(request, _('Incorrect Form'),
                       extra_tags="alert-danger")
        return redirect(reverse('create_user'))


class UpdateUser(CheckAuthentication, View):

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.id != kwargs.get('pk'):
            messages.error(request, _('You do not have rights to change another user.'),
                           extra_tags="alert-danger")
            return redirect(reverse('user_list'))

        user_id = user.id
        form = UsersForm(instance=user)
        return render(request, 'users/update.html',
                      {'form': form, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = UsersForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, _('User changed successfully'),
                             extra_tags="alert-success")
            return redirect(reverse('user_list'))

        user_id = user.id
        messages.error(request, _('Incorrect Form'),
                       extra_tags="alert-danger")
        return render(request, 'users/update.html',
                      {'form': form, 'user_id': user_id})


class DeleteUser(CheckAuthentication, DeleteView):

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.id != kwargs.get('pk'):
            messages.error(request, _(
                'You do not have rights to change another user.'),
                           extra_tags="alert-danger")
            return redirect(reverse('user_list'))

        return render(request, 'users/delete.html', {
                          'user': user, 'user_id': user.id})

    def post(self, request, *args, **kwargs):

        user = request.user
        if user:
            messages.success(request, _('User deleted successfully'),
                             extra_tags="alert-success")
            user.delete()
        return redirect(reverse('user_list'))
