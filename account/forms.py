from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UpdateForm(forms.ModelForm):
	class Meta:
		model = User 
		field = ['username', 'first_name', 'last_name', 'email']
		exclude = ['password1', 'password2']

class LoginForm(forms.Form):
	class Meta:
		model = User
		fields = ['username', 'password']
		exclude = ['first_name', 'last_name', 'email']

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)