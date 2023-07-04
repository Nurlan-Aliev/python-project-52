from django import forms
from task_manager.tasks.models import TasksModel
from task_manager.statuses.models import StatusModel
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from task_manager.labels.models import LabelModel


class TasksForm(forms.ModelForm):

    name = forms.CharField(max_length=100, label=_('Name'),
                           widget=forms.TextInput(
                               attrs={'placeholder': _('Name'),
                                      'id': 'id_name',
                                      'class': 'form-control'}))

    description = forms.CharField(required=False, label=_('Description'),
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                             'placeholder': _('Description')}))

    status = forms.ModelChoiceField(
        queryset=StatusModel.objects.all(), label=_('Status'),
        widget=forms.Select(
            attrs={'class': 'form-select'}))

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(), label=_('Executor'), required=False,
        widget=forms.Select(
            attrs={'class': 'form-select'}))

    labels = forms.ModelMultipleChoiceField(
        queryset=LabelModel.objects.all(), label=_('label'),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

    class Meta:
        model = TasksModel
        fields = ['name', 'description', 'status', 'executor', 'labels']
