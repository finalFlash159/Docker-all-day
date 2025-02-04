from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    your_name = forms.CharField(max_length=150, required=True, label="Your Name")

    class Meta:
        model = User
        fields = ['username', 'your_name', 'password1', 'password2']
