from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Detail,User

def home(request: HttpRequest):
    mail=request.COOKIES.get('email',None)
    if(mail is None):
        return redirect('login')
    
    user=User.objects.filter(email=mail)
    if(len(user)==0):
        return redirect('login')
    
    id=user[0].id
    

    params={'id':id}
    return render(request,'home.html',params)

def profile(request: HttpRequest):
    userDetails :Detail

    uid=request.GET.get('uid',None)
    if(uid is not None and len(uid)==0):
        uid=None

    if(uid is None):
        return HttpResponse("User Not Found")

    userDetails=Detail.objects.filter(user_id=uid)[0]
    fname=userDetails.user.firstName
    lname=userDetails.user.lastName
    mail=userDetails.user.email
    phone=userDetails.user.phNo
    gender='Male' if userDetails.user.gender else 'Female'
    dp=userDetails.profilePicture
    bio=userDetails.bio
    params={
        'fname':fname,
        "lname":lname,
        'mail':mail,
        'phone':phone,
        'gender':gender,
        'dp':dp,
        'bio':bio,
        'mydp':""
    }

    return render(request,'profile.html',params)