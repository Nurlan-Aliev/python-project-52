from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label=_('Name'),
                                 widget=forms.TextInput(
                                     attrs={'id': 'id_first_name',
                                            'class': 'form-control mb-3',
                                            'placeholder': _('Name')}))

    last_name = forms.CharField(max_length=50, label=_('Surname'),
                                widget=forms.TextInput(
                                    attrs={'id': 'id_last_name',
                                           'class': 'form-control mb-3',
                                           'placeholder': _('Surname')}))

    username = forms.CharField(label=_('username'), widget=forms.TextInput(
        attrs={'id': 'id_username',
               'class': 'form-control mb-3',
               'placeholder': _('username')}))

    password1 = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'id': 'id_password1',
                   'class': 'form-control mb-3',
                   'placeholder': _('password')}))

    password2 = forms.CharField(
        label=_('Password confirmation'), widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'id': 'id_password2',
                   'class': 'form-control mb-3',
                   'placeholder': _('Password confirmation')}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        queryset = User.objects.exclude(pk=self.instance.pk)
        if queryset.filter(username=username).exists():
            raise forms.ValidationError(_('This username is already taken.'))
        return username

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'password1',
                  'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'id': 'id_username',
                   'class': 'form-control',
                   'placeholder': _('username')}))

    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={'id': 'id_password',
                   'class': 'form-control',
                   'placeholder': _('password')}))

    class Meta:
        model = User
        fields = ('username', 'password')
