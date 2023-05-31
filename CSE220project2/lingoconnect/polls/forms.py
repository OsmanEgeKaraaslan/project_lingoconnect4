from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=150, help_text='Required. 150 characters or fewer.')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text='Your password must contain at least 8 characters. Your password can’t be entirely numeric.')
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput,
                                help_text='Please enter your password again.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)