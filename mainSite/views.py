from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Detail, Friend, Post,User
from . import viewHelpers 

def getPosts(id :int):
    #TODO add only friends post logic later
    #TODO sort by created date
    #TODO add Name and dp of author
    posts=Post.objects.all()
    #print(dir(posts[0]))
    return posts


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
    posts=getPosts(id)
    params={'myid':id,'mydp':dp,'posts':posts}
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
        
    flist=viewHelpers.getUserData([user[0] for user in Friend.objects.get(this=uid).others.values_list()])
    followers=viewHelpers.getUserData([user[0] for user in Friend.objects.filter(others=uid).values_list()])















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
        'mydp':mydp,
        'flist':flist,
        'followers':followers
    }

    return render(request,'profile.html',params)


def friends(request:HttpRequest,message=""):
    if(request.method=="POST"):
        myid=request.POST.get('myid',0)
        other=request.POST.get('userid',0)
        if(0 in (myid,other)):
            redirect('/')
        return viewHelpers.evalWith(myid,other)

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
        fl=Friend.objects.get(this=details.user_id).others.values_list()
        user['flist']=[f[0]for f in fl]
        
        user['profilePicture']=details.profilePicture
        user['bio']=details.bio
        ulist.append(user)
    
    if(request.method=="GET"):
        ss=request.GET.get('s',"")
        ulist=list(viewHelpers.sortQ(ulist,ss))

    users=ulist
    del ulist
    friendList=[ friend[0] for friend in friendList]
    params={'myid':id,'mydp':dp,'users':users,'friendList':friendList}
    return render(request,'friends.html',params)





