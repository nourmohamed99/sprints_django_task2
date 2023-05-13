from django.db import models

# Create your models here.
class Student(models.Model):
	f_name = models.CharField(max_length=255)
	l_name = models.CharField(max_length=255)
	gender = models.CharField(max_length=2)
	age = models.IntegerField()
	birth_date = models.DateField()

class Course(models.Model):
	name = models.CharField(max_length=255)
	num_students = models.IntegerField()
	
