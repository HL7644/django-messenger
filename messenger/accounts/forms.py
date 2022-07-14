from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    username=forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'type':'text',
        'class': 'form-control my-2',
        'placeholder': 'Username'
    }))
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'type':'password',
        'class':'form-control my-2',
        'placeholder': 'password',
    }))
    password2=forms.CharField(label="Password Confirmation", widget=forms.PasswordInput(attrs={
        'type':'password',
        'class':'form-control my-2',
        'placeholder': 'password',
    }))
    class Meta:
        model=User
        fields=[
            'username',
            'password1',
            'password2',
        ]

class LogInForm():
    username=forms.CharField()