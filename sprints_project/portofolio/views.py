from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Course
from .models import Student
from django.views.generic.list import ListView
 

def cv(request):
	template = loader.get_template("cv.html")
	return HttpResponse(template.render())
	#return render(request, "show.html")

class StudentList(ListView):
	model = Student

def course(request):
	context ={}
	context['dataset'] = Course.objects.all()
	return render(request, "courses.html",context)