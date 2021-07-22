from django import forms
from .models import Student
from django.forms import ModelForm

class StuForm(ModelForm):
	class Meta:
		model=Student
		fields='__all__'