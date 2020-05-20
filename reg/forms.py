from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=25, label="First Name")
    last_name = forms.CharField(max_length=25, label="Last Name")
    email = forms.EmailField(max_length=50, label="Email")
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2']