from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    #TODO identify if cookie is there and go to login or signup accordingly
    return login(request)

def login(request):
    params={'Title':'Login'}
    return render(request,'login.html')

def about(request):
    params={'Title':'About Us'}
    return render(request,'about.html')

def signin(request):
    params={'Title':'SignIn'}
    return render(request,'signin.html')

def home(request):
    params={'Title':'Home'}
    return render(request,'home.html')

def createId(request):
    
    return HttpResponse('Created')