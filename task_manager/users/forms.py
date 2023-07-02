from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UsersForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label='Name')
    last_name = forms.CharField(max_length=50)
    password1 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'password1',
                  'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')
