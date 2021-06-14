from django.shortcuts import render

def login(request):
    #TODO identify if cookie is there and go to login or signup accordingly
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def signin(request):
    return render(request,'signin.html')

def home(request):
    return render(request,'home.html')

