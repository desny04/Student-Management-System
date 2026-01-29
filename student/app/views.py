from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    stds=Students.objects.all()
    course=[]
    if request.method=='POST':
        course=request.POST['course']
        stds=Students.objects.fiter(course=course)
    return render(request,'index.html',{'stds':stds,'course':course})
