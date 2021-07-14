from django.urls import path
from anitsapp import views

urlpatterns = [
    path('demo',views.demo,name="demo")
    ]