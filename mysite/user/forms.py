from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_first_name', 'user_last_name', 'user_name', 'user_cellphone', 'user_password', 'user_profile_image']