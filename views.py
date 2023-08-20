from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django import forms


# Create your views here.
def index (request):
    baseinfo=basicinfo.objects.all()
    expwork=workexp.objects.all()
    edu =education.objects.all()
    ref=references.objects.all()
    
    context={
        "baseinfo":baseinfo,
        "workexp":expwork,
        "education":edu,
        "refrence":ref,
        
    }
    return render(request,'index.html',context)


def contactform(request):
    if request.method == 'POST':
        name =request.POST.get('name')
        print(name)
        subject =request.POST.get('Subject')
        email =request.POST.get('_reeplyto')
        message =request.POST.get('message')
        sbt=ContactSubmission(name=name,subject=subject,email=email,message=message)
        sbt.save()
        
      
        return render(request, 'index.html')
    
    












