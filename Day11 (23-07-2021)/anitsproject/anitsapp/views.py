from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,upload
from .forms import StuForm,uploadForm
from anitsproject import settings
from django.core.mail import send_mail
from django.contrib import messages
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

def mailsending(request):
	p=Student.objects.values_list("emailid",flat=True)
	print(p)
	if request.method=='POST':
		sb=request.POST['sub']
		mg=request.POST['msg']
		snd=settings.EMAIL_HOST_USER
		t=send_mail(sb,mg,snd,p)
		if t==1:
			messages.success(request,"mail send to {} succesfully".format(p))
			return redirect('/mailsending')
		messages.warning(request,"mail doesn't send")
	return render(request,'anitsapp/mailsend.html')

def upload(request):
	if request.method=='POST':
		form=uploadForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,"Uploaded succesfully")
	form=uploadForm()
	return render(request,'anitsapp/upload.html',{'form':form})