from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StuForm
# Create your views here.
def Homeurl(request):
	details={
	'name':'python',
	'company':'apssdc',
	'place':'vijayawada',
	'mobileno':'123546767',
	'emailid':'apssdc@gmail.com'
	}
	return render(request,'anitsapp/home.html',{'Name':'Pavani','details':details})


def about(request):
	return render(request,'anitsapp/about.html')

def contact(request):
	return render(request,'anitsapp/contact.html')

def studetails(request):
	data=Student.objects.all()
	return render(request,'anitsapp/studetails.html',{'data':data})

def register(request):
	if request.method=='POST':
		form=StuForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('studetails')
	form=StuForm()
	return render(request,"anitsapp/register.html",{'form':form})