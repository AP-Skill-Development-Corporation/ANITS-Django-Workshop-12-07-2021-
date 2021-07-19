from django.shortcuts import render,redirect
from django.http import HttpResponse
from FormApp.models import Register
from FormApp.forms import Reg
# Create your views here.
def demo(request):
	return HttpResponse("this is formapp")

def register(request):
	if request.method=="POST":
		formdata=Reg(request.POST)
		if formdata.is_valid():
			formdata.save()
	formdata=Reg()
	return render(request,'FormApp/register.html',{'data':formdata})

def details(request):
	data=Register.objects.all()
	return render(request,'FormApp/details.html',{'data':data})


def update(request,id):
	a=Register.objects.get(id=id)
	if request.method=="POST":
		u=Reg(request.POST,instance=a)
		if u.is_valid():
			u.save()
			return redirect('/form/details')
	u=Reg(instance=a)
	return render(request,'FormApp/update.html',{'u':u})


def delete(request,id):
	d=Register.objects.get(id=id)
	if request.method=="POST":
		d.delete()
		return redirect('/form/details')
	return render(request,'FormApp/delete.html',{'d':d})
