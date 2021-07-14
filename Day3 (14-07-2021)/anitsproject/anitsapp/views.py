from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def static(request):
	return HttpResponse("<h1><center>welcome to staticpage</center></h1>")


def dynamicstr(request,name):
	return HttpResponse("<h1><center>your name:"+name+"</center></h1>")

def dynamicint(request,rollno):
	return HttpResponse("<h1><center>your rollno: {}</center></h1>".format(rollno))


def dynamic(request,name,rollno,branch):
	return HttpResponse("<h1><center>your name: {}</center></h1></n><h1><center>your rollno: {}</center></h1></n><h1><center>your branch: {}</center></h1>".format(name,rollno,branch))

def demo(request):
	return HttpResponse("<h1><center>DemoPage</center></h1>")