from django import forms
from task_manager.statuses.models import StatusModel


class StatusForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Name',
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Name'},
                           ))


    class Meta:
        model = StatusModel
        fields = ['name']
