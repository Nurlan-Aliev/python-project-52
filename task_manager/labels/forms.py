from django import forms
from task_manager.labels.models import LabelModel
from django.utils.translation import gettext as _


class LabelForms(forms.ModelForm):
    name = forms.CharField(max_length=100, label=_('Name'),
                           widget=forms.TextInput(
                               attrs={'placeholder': _('Name'),
                                      'id': 'id_name',
                                      'class': 'form-control mb-3'}))

    class Meta:
        model = LabelModel
        fields = ['name']
