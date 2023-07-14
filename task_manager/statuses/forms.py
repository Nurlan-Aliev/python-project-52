from django import forms
from task_manager.statuses.models import StatusModel
from django.utils.translation import gettext as _


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100, label=_('Name'),
        widget=forms.TextInput(
            attrs={'id': 'id_name',
                   'class': 'form-control', 'placeholder': _('Name')}))

    class Meta:
        model = StatusModel
        fields = ['name']
