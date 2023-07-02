from django import forms
from task_manager.tasks.models import TasksModel
from task_manager.statuses.models import StatusModel
from django.contrib.auth.models import User
from django.utils.translation import gettext as _



class TasksForm(forms.ModelForm):

    name = forms.CharField(max_length=100, label=_('Name'),
                           widget=forms.TextInput(
                               attrs={'placeholder': _('Name'), 'id': 'id_name'}))
    description = forms.TextInput()
    status_id = forms.ModelChoiceField(queryset=StatusModel.objects.all(), label=_('Status'))
    executor_id = forms.ModelChoiceField(queryset=User.objects.all(), label=_('Executor'))

    class Meta:
        model = TasksModel
        fields = ['name', 'description', 'status_id', 'executor_id']


