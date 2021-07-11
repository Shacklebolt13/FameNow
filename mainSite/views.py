from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Detail, Friend,User

def home(request: HttpRequest):
    #TODO additional check for login using csrf or some encryption
    id=request.COOKIES.get('id',None)
    if(id is None):
        return redirect('login')
    
    user=User.objects.filter(id=id)
    if(len(user)==0):
        return redirect('login')
    
    id=user[0].id

    dp=Detail.objects.filter(user_id=id)[0].profilePicture
    
    url=request.build_absolute_uri()
    profileUri=''

    if('home' in url):
        profileUri=f'profile?uid={id}'
    else:
        profileUri=f'home/profile?uid={id}'
    
    if(not url.endswith('/')):
        url+="/"
    url=url+profileUri

    params={'profileUrl':url,'mydp':dp}
    return render(request,'home.html',params)

def profile(request: HttpRequest):
    userDetails :Detail

    uid=request.GET.get('uid',None)
    print(uid)
    if(uid is not None and len(uid)==0):
        uid=None

    if(uid is None):
        return HttpResponse("""User Not Found  <a href="/home/">HOME</a> """) 

    userDetails=Detail.objects.filter(user=uid)
    if(len(userDetails)==0):
        return HttpResponse("""User Not Found  <a href="/home/">HOME</a> """)  
    userDetails=userDetails[0]
    fname=userDetails.user.firstName
    lname=userDetails.user.lastName
    mail=userDetails.user.email
    phone=userDetails.user.phNo
    gender='Male' if userDetails.user.gender else 'Female'
    dp=userDetails.profilePicture
    bio=userDetails.bio

    myId=request.COOKIES.get('id',None)
    myProfile=request.build_absolute_uri().split('=')[0]+f"={myId}"
    if(myId is None):
        mydp='images/unknownUser.png'
    else:
        me=Detail.objects.filter(user=myId)
       
        if(len(me)==0):
            mydp='images/unknownUser.png'
        else:
            me=me[0]
            mydp=me.profilePicture
    
    params={
        'myProfile':myProfile,
        'id':myId,
        'fname':fname,
        "lname":lname,
        'mail':mail,
        'phone':phone,
        'gender':gender,
        'dp':dp,
        'bio':bio,
        'mydp':mydp
    }

    return render(request,'profile.html',params)


def friends(request:HttpRequest,message=""):
    id=request.COOKIES.get('id',None)
    if(id is None):
        redirect('/')
    user=Detail.objects.filter(user_id=id)
    if(len(user)==0):
        redirect('/')

    user=user[0]

    id=user.user_id
    dp=user.profilePicture
    users=User.objects.all().values()
    friendList=Friend.objects.get(this=id).others.values_list()
    #print(friendList,'\n\n\n',dir(friendList))
    ulist=[]
    for user in users:
        if(user['id']==id):
            continue;

        details=Detail.objects.get(user_id=user['id'])
        user['profilePicture']=details.profilePicture
        user['bio']=details.bio
        ulist.append(user)
    users=ulist
    del ulist
    friendList=[ friend[0] for friend in friendList]
    print(friendList)
    params={'myid':id,'mydp':dp,'users':users,'friendList':friendList}
    return render(request,'friends.html',params)