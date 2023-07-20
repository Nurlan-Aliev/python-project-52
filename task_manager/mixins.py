from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django import forms
import django_filters
from django.contrib.messages.views import SuccessMessageMixin


class UserPassMixin(UserPassesTestMixin):
    redirect_field_name = None
    raise_exception = False
    permission_denied_message = _("You have no right to edit the user.")

    def test_func(self):
        user = self.get_object()
        return user == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, _("You have no right to edit the user."))
            return redirect(reverse_lazy('user_list'))


class AppLoginMixin(LoginRequiredMixin, SuccessMessageMixin):
    redirect_field_name = None
    success_message = _('You are not authorized! Please sign in.')
    raise_exception = False


class UserChoiceFieldMixin(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class UserFiletFieldMixin(django_filters.ModelChoiceFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.label_from_instance =\
            lambda obj: f"{obj.first_name} {obj.last_name}"


