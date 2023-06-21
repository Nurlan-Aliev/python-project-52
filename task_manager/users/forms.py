from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsersForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, label='Name')
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',  'password1', 'password2')
