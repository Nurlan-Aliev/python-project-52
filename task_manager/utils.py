from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django import forms
import django_filters
from django.contrib.messages.views import SuccessMessageMixin


class AppLoginMixin(LoginRequiredMixin, SuccessMessageMixin):
    redirect_field_name = None
    login_url = reverse_lazy('login')
    success_message = _('You are not authorized! Please sign in.')


class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class UserFiletField(django_filters.ModelChoiceFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.label_from_instance =\
            lambda obj: f"{obj.first_name} {obj.last_name}"
