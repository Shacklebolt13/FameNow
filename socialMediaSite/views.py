from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from mainSite.models import User
import datetime
from django.conf import settings
import bcrypt

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

def home(request):
    params={}
    return render(request,'home.html',params)

def createId(request):
    confHidden(request)
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    phone=request.POST.get('phone')
    mail=request.POST.get('mail')
    password=hashPass(request.POST.get('pass'))
    gender=request.POST.get('gender')
    gender=True if gender=="true" else False
    salt=bcrypt.gensalt()
    print(salt)

    if(gender):
        dp="images/defaultMan.png"
    else:
        dp="images/defaultWoman.png"

    user=User(firstName=fname,lastName=lname,phNo=phone,email=mail,password=password,gender=gender,profilePicture=dp)
    print(user)
    user.save()
    response= redirect('/')
    response.set_cookie('email',mail,7,datetime.datetime.now()+datetime.timedelta(days=7))  #expires a week later
    return response

def loginAction(request):
    confHidden(request)
    return


def confHidden(request : HttpRequest):
    #TODO confirm using referer
    if(not request.META.get('HTTP_REFERER',False)):
       raise Http404() 


def checkLoginStatus(request):
    
    if('email' in request.COOKIES):
        print('all ok')
        try:
            mail=User.objects.get(email=request.COOKIES['email']).email
        except Exception:
            return False
        return True 
    else:
        return False
    
def hashPass(password :str):
    #TODO create hashing algorithm
    return password