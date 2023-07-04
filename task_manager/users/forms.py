from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _


class UsersForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label=_('Name'),
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'placeholder': _('Name')}))
    last_name = forms.CharField(max_length=50, label=_('Surname'),
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': _('Surname')}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': _('username')}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': _('password')}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': _('password')}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'password1',
                  'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('username')}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('password')}))

    class Meta:
        model = User
        fields = ('username', 'password')
