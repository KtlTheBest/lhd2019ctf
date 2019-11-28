from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, min_length=3, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))

    password = forms.CharField(max_length=40, min_length=5, widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password')
