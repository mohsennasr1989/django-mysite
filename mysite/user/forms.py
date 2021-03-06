from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CustomUser


class SignUpForm(UserCreationForm):
    # firstname = forms.TextInput()
    # lastname = forms.TextInput()
    # profile = forms.FileField()
    # cellphone = forms.NumberInput()
    # email = forms.EmailField()

    class Meta:
        model = User
        # fields = ['user_id', 'firstname', 'lastname', 'user.username', 'cellphone', 'user.password1', 'user.password2',
        #           'profile', 'create_date', 'last_login_date']
        fields = ['username', 'password1', 'password2']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['username', 'create_date', 'last_login_date']
