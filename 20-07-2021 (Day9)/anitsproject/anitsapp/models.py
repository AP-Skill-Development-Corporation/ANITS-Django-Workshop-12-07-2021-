from django.db import models

# Create your models here.
class Student(models.Model):
	colleges=(('anits','anits'),('vvit','vvit'),('iiit','iiit'))
	years=(('1','1'),('2','2'),('3','3'),('4','4'))
	Name=models.CharField(max_length=100)
	Rollno=models.CharField(unique=True,max_length=20)
	College=models.CharField(max_length=10,choices=colleges)
	year=models.CharField(max_length=10,choices=years)


	def __str__(self):
		return self.Name+"-"+self.Rollno+"-"+self.College
