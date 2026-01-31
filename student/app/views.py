from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        std=Students.objects.filter(uname=request.user.pk)
        print(std)
        return render(request,'index.html',{'std':std})
    else:
        return redirect(loginUser)

def addStudents(request):
    if request.user.is_authenticated:
        courses=Courses.objects.all()
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            age=request.POST['age']
            phone=request.POST['phone']
            course=request.POST['course']
            cname=Courses.objects.get(cname=course)
            data=Students.objects.create(name=name,age=age,email=email,phone=phone,cname=cname,uname=request.user)
            data.save()
        return render (request,'addStudents.html',{'courses':courses})
    else:
        return redirect(loginUser)

def editStudents(request,pk):
    std=Students.objects.get(pk=pk)
    courses=Courses.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        phone=request.POST['phone']
        course=request.POST['course']
        cname=Courses.objects.get(cname=course)
        Students.objects.filter(pk=pk).update(name=name,age=age,email=email,phone=phone,cname=cname)
        return redirect(index)
    return render (request,'editStudents.html',{'std':std,'courses':courses})

def deleteStudents(request,pk):
    Students.objects.get(pk=pk).delete()
    return redirect(index)

def registerUser(request):
    if request.method=='POST':
        name=request.POST['firstname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cnf_password=request.POST['cnf_password']
        if password==cnf_password:
            data=User.objects.create_user(first_name=name,username=username,email=email,password=password)
            data.save()
            return redirect(loginUser)
        else:
            print('Password does not match')
    return render(request,'reigster.html')


def loginUser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(index)
        else:
            print('Username or password is incorrect')
            return redirect(loginUser)
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect(loginUser)
    
