from django.http.response import HttpResponse
from django.shortcuts import render

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
    
    return HttpResponse('Created')


def loginAction(request):

    return HttpResponse('loginAction')