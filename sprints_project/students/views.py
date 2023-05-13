from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import Student
from django.views.generic.list import ListView


def Welcome(request):
	return HttpResponse("welcome to our site")

def Show(request):
    
    # template = loader.get_template('show.html')
    # return HttpResponse(template.render())	
    today = datetime.datetime.now().date()
    return render(request,"show.html", {"today" : today}) 

def list_view(request):
	context ={}
	context['dataset'] = Student.objects.all()
	return render(request, "list_view.html",context)

class StudentList(ListView):
	model = Student