from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _


class CheckAuthentication(LoginRequiredMixin):
    redirect_field_name = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request,
                             _('You are not authorized! Please sign in.'),
                             extra_tags="alert-danger")
        return super().dispatch(request, *args, **kwargs)