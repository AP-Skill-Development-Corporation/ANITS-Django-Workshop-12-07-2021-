from django.urls import path
from FormApp import views
urlpatterns = [
	path('demo/',views.demo),
	path('register/',views.register,name='register'),
	path('details/',views.details,name='details'),
	path('update/<int:id>/',views.update,name='update'),
	path('delete/<int:id>/',views.delete,name='delete'),
	





]