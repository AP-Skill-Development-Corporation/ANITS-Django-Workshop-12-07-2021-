from django import forms
from .models import Student,upload
from django.forms import ModelForm

class StuForm(ModelForm):
	class Meta:
		model=Student
		fields='__all__'

class uploadForm(ModelForm):
	class Meta:
		model=upload
		fields='__all__'
