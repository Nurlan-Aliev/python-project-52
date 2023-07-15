from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, UpdateView
from django.utils.translation import gettext as _
from task_manager.users.forms import UsersForm
from task_manager.utils import CheckAuthentication


class Users(View):
    template_name = 'users/users.html'

    def get(self, request):
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
            return redirect(reverse_lazy('login'))

        messages.error(request, _('Incorrect Form'),
                       extra_tags="alert-danger")
        return render(request, self.template_name, {'form': form})


class UpdateUser(CheckAuthentication, View):
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_list')

    def get(self, request, *args, **kwargs):
        user = request.user
        pk = kwargs.get('pk')
        if user.id != kwargs.get('pk'):
            messages.error(request, _(
                'You do not have rights to change another user.'),
                extra_tags="alert-danger")
            return redirect(self.success_url)

        form = UsersForm(instance=user)
        return render(request, self.template_name,
                      {'form': form, 'pk': pk})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = UsersForm(request.POST, instance=user)
        pk = kwargs.get('pk')
        if user.id != kwargs.get('pk'):
            messages.error(request, _(
                'You do not have rights to change another user.'),
                extra_tags="alert-danger")
            return redirect(self.success_url)
        if form.is_valid():
            form.save()
            messages.success(request, _('User changed successfully'),
                             extra_tags="alert-success")
            return redirect(self.success_url)

        return render(request, self.template_name,
                      {'form': form, 'pk': pk})


class DeleteUser(CheckAuthentication, DeleteView):
    template_name = 'users/delete.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        user_id = kwargs.get('pk')
        if user.id != kwargs.get('pk'):
            messages.error(request, _(
                'You do not have rights to change another user.'),
                extra_tags="alert-danger")
            return redirect(reverse_lazy('user_list'))

        return render(request, self.template_name,
                      {'user': user, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user = request.user

        if user.id != kwargs.get('pk'):
            messages.error(request, _(
                'You do not have rights to change another user.'),
                extra_tags="alert-danger")
            return redirect(reverse_lazy('user_list'))

        elif user.author_id.exists() or user.executor_id.exists():
            messages.success(request, _("Can't delete user because it used"),
                             extra_tags="alert-danger")

        else:
            messages.success(request, _('User deleted successfully'),
                             extra_tags="alert-success")

            user.delete()

        return redirect(reverse_lazy('user_list'))
