from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def Homeurl(request):
	return render(request,'anitsapp/home.html')