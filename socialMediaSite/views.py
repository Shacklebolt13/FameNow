from django.http import response
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from mainSite.models import User
import datetime
from django.conf import settings
import bcrypt
import sys
from django.db import IntegrityError
from mainSite.views import home

def index(request):
    if(checkLoginStatus(request)):
        return home(request)
    else:
        response=login(request)
        response.delete_cookie('email')
        return response


def login(request):
    params={}
    return render(request,'login.html',params)


def about(request):
    params={}
    return render(request,'about.html',params)


def signin(request):
    params={}
    return render(request,'signin.html',params)


def createId(request):
    confHidden(request)

    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    phone=request.POST.get('phone')
    mail=request.POST.get('mail')
    password=request.POST.get('pass')
    gender=request.POST.get('gender')

    gender=True if gender=="true" else False
    salt=bcrypt.gensalt()
    password=bcrypt.hashpw(password.encode('utf-8'),salt)
    password=str(password,encoding='utf-8')
    
    user=User(firstName=fname,lastName=lname,phNo=phone,email=mail,password=password,gender=gender)
    try:
        user.save()
    except IntegrityError:
        params={'message':'email already exists'}
        return render(request,'signin.html',params)

    
    response= redirect('/')
    response.set_cookie('email',mail,7,datetime.datetime.now()+datetime.timedelta(days=7))  #expires a week later
    
    return response


def loginAction(request : HttpRequest):
    confHidden(request)
    mail=request.POST.get('mail',False)
    password=request.POST.get('pass',False)
    print(mail,password)
    user=User.objects.filter(email=mail)
    if(len(user)!=0):
        hashed=user[0].password.encode('utf-8')
        if(bcrypt.checkpw(password.encode('utf-8'),hashed)):
            response=home(request)
            response.set_cookie('email',mail,7,datetime.datetime.now()+datetime.timedelta(days=7))  #expires a week later
            return response

    return redirect('login')


def confHidden(request : HttpRequest):
    #TODO confirm using referer
    if(not request.META.get('HTTP_REFERER',False)):
       raise Http404() 


def checkLoginStatus(request):
    
    if('email' in request.COOKIES):
        try:
            mail=User.objects.get(email=request.COOKIES['email']).email
        except Exception:
            return False
        return True 
    else:
        return False