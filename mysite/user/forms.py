from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'cellphone', 'password',
                  'profile']


class SignUpForm(UserCreationForm):
    firstname = forms.TextInput()
    lastname = forms.TextInput()
    profile = forms.FileField()
    cellphone = forms.NumberInput()

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'password', 'cellphone', 'profile']