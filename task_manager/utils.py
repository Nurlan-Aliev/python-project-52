from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django import forms


class CheckAuthentication(LoginRequiredMixin):
    redirect_field_name = None
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request,
                             _('You are not authorized! Please sign in.'),
                             extra_tags="alert-danger")
        return super().dispatch(request, *args, **kwargs)


class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"
