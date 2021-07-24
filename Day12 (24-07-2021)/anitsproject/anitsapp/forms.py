from django import forms
from .models import Student,upload
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StuForm(ModelForm):
	class Meta:
		model=Student
		fields='__all__'

class uploadForm(ModelForm):
	class Meta:
		model=upload
		fields='__all__'

class authuserform(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter confirm password'}))
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username','required':True}),
		"email":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your emailid','required':True}),
		}

