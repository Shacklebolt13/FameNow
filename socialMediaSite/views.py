from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from mainSite.models import User

def index(request):
    #TODO identify if cookie is there and go to login or signup accordingly
    return login(request)

def login(request):
    params={'pgTitle':'Login'}
    return render(request,'login.html',params)

def about(request):
    params={'pgTitle':'About Us'}
    return render(request,'about.html',params)

def signin(request):
    params={'pgtitle':'SignIn'}
    return render(request,'signin.html',params)

def home(request):
    params={'pgTitle':'Home'}
    return render(request,'home.html',params)

def createId(request):
    if(not confHidden(request)):
        raise Http404()

    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    phone=request.POST.get('phone')
    mail=request.POST.get('mail')
    password=request.POST.get('pass')
    gender=request.POST.get('gender')
    gender=True if gender=="true" else False
    
    if(gender):
        dp="images/defaultMan.png"
    else:
        dp="images/defaultWoman.png"

    user=User(firstName=fname,lastName=lname,phNo=phone,email=mail,password=password,gender=gender,profilePicture=dp)
    print(user)
    user.save()
    return HttpResponse('Created')


def loginAction(request):

    return HttpResponse('loginAction')


def confHidden(request):
    #TODO confirm using referer
    return True