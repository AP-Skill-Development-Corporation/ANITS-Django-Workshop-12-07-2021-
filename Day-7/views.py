from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp.models import Student
# Create your views here.

def sample(request):
	return HttpResponse("hi,welcome to django session")

def home(request):
	return HttpResponse("<h3><center>hi...guys</center></h3>")

def dynamic(request,id,name):
	return HttpResponse("my Id is {} and My Name is {}".format(id,name))

def temp(request):
	return render(request,'myApp/temp.html')

def table(request):
	return render(request,'myApp/table.html')

def inline(request):
	return render(request,'myApp/inline.html')

def internal(request):
	return render(request,'myApp/internal.html')

def external(request):
	return render(request,'myApp/external.html')

def boot(request):
	return render(request,'myApp/boot.html')

def register(request):
	return render(request,'myApp/register.html')

def offline(request):
	return render(request,'myApp/offline.html')

def offline2(request):
	return render(request,'myApp/offline2.html')


def reg(request):
	if request.method=="POST":
		na=request.POST['name']
		num=request.POST['rollnum']
		age=request.POST['age']
		mob=request.POST['mobile']
		em=request.POST['email']
		addr=request.POST['addr']
		Student.objects.create(name=na,rollnum=num,age=age,
			mobile=mob,email=em,address=addr)
		# return HttpResponse("your data is added successfully")
		return redirect('/display')
	return render(request,'myApp/reg.html')


def display(request):
	data=Student.objects.all()
	return render(request,'myApp/display.html',{'data':data})

def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.name=request.POST['name']
		data.rollnum=request.POST['rollnum']
		data.age=request.POST['age']
		data.mobile=request.POST['mobile']
		data.email=request.POST['email']
		data.address=request.POST['addr']
		data.save()
		return redirect('/display')
	return render(request,'myApp/update.html',{'data':data})


def delete(request,id):
	ob=Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/display')
	return render(request,'myApp/delete.html',{'info':ob})