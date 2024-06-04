from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
def home(request):
    students=Student.objects.all()
    return render(request,'home.html',{'students':students})
def student(request,student_id):
    try:

        student=Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        student=None
    return render(request,'student.html',{'student':student})