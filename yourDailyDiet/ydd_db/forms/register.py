from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    bot_username = forms.CharField(widget=forms.HiddenInput(), required=False)
    bot_user_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
