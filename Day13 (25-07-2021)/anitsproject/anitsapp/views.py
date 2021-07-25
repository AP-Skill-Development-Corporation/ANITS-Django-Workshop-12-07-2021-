from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,upload
from .forms import StuForm,uploadForm,authuserform,updateform
from django.contrib.auth.models import User
from anitsproject import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def Homeurl(request):
	# details={
	# 'name':'python',
	# 'company':'apssdc',
	# 'place':'vijayawada',
	# 'mobileno':'123546767',
	# 'emailid':'apssdc@gmail.com'
	# }
	return render(request,'anitsapp/home.html')


def about(request):
	return render(request,'anitsapp/about.html')

def contact(request):
	return render(request,'anitsapp/contact.html')

@login_required
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

@login_required
def mailsending(request):
	p=User.objects.values_list("email",flat=True)
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


@login_required
def upload(request):
	if request.method=='POST':
		form=uploadForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,"Uploaded succesfully")
	form=uploadForm()
	return render(request,'anitsapp/upload.html',{'form':form})

def authreg(request):
	if request.method=='POST':
		form=authuserform(request.POST)
		if form.is_valid:
			form.save()
			messages.success(request,'Hi '+request.POST['username']+'....you are successfully registered')
			messages.info(request,request.POST['username']+' ! Now you can login')
			return redirect('/authreg')
	form=authuserform()
	return render(request,'anitsapp/authreg.html',{'form':form})

@login_required
def dashboard(request):
	return render(request,'anitsapp/dashboard.html')

@login_required
def profile(request):
	return render(request,'anitsapp/profile.html')

@login_required
def update(request):
	if request.method=="POST":
		form=updateform(request.POST,instance=request.user)
		if form.is_valid:
			form.save()
			messages.success(request,"{} your details updated successfully".format(request.user.username))
			return redirect('/profile')
	form=updateform(instance=request.user)
	return render(request,'anitsapp/update.html',{'form':form})