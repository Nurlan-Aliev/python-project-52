from django import forms
from task_manager.tasks.models import TasksModel
from task_manager.statuses.models import StatusModel
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from task_manager.labels.models import LabelModel
import django_filters
from task_manager.utils import UserChoiceFieldMixin, UserFiletFieldMixin


class TasksForm(forms.ModelForm):

    name = forms.CharField(max_length=100, label=_('Name'),
                           widget=forms.TextInput(
                               attrs={'placeholder': _('Name'),
                                      'id': 'id_name',
                                      'class': 'form-control mb-3'}))

    description = forms.CharField(
        required=False, label=_('Description'),
        widget=forms.Textarea(
            attrs={'class': 'form-control mb-3',
                   'id': 'id_description',
                   'placeholder': _('Description')}))

    status = forms.ModelChoiceField(
        queryset=StatusModel.objects.all(), label=_('Status'),
        widget=forms.Select(
            attrs={'id': 'id_status',
                   'class': 'form-select mb-3'}))

    executor = UserChoiceFieldMixin(
        queryset=User.objects.all(), label=_('Executor'),
        required=False,

        widget=forms.Select(
            attrs={'id': 'id_executor',

                   'class': 'form-select mb-3'}))

    labels = forms.ModelMultipleChoiceField(
        queryset=LabelModel.objects.all(), label=_('labels'),
        required=False,
        widget=forms.SelectMultiple(attrs={'id': 'id_labels',
                                           'class': 'form-select mb-3'})
    )

    class Meta:
        model = TasksModel
        fields = ['name', 'description', 'status', 'executor', 'labels']


class FilterForm(django_filters.FilterSet):

    status = django_filters.ModelChoiceFilter(
        queryset=StatusModel.objects.all(), label=_('Status'),
        widget=forms.Select(
            attrs={'id': 'id_status',
                   'class': 'form-select mb-3'}))

    executor = UserFiletFieldMixin(

        queryset=User.objects.all(), label=_('Executor'), required=False,
        widget=forms.Select(
            attrs={'id': 'id_executor',
                   'class': 'form-select mb-3'}))

    labels = django_filters.ModelChoiceFilter(
        queryset=LabelModel.objects.all(), label=_('label'),
        required=False,
        widget=forms.Select(attrs={'id': 'id_labels',
                                   'class': 'form-select mb-3'}))

    def filter_is_mine(self, queryset, name, value):
        lookup = queryset.filter(author=self.request.user)
        return lookup if value else queryset

    author = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(attrs=({'id': 'id_self_tasks',
                                           'class': 'form-check-input',
                                           })),
        method='filter_is_mine',
        label=_('Only your tasks'))

    class Meta:
        model = TasksModel
        fields = ['status',
                  'executor',
                  'labels',
                  'author'
                  ]
