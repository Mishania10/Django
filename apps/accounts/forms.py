from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'full_name', 'email')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=150)
