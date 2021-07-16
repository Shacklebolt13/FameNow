from mainSite.models import Detail, Friend, User
from django.http import HttpRequest
from django.shortcuts import redirect, render

def sortQ(ulist:list,search:str):
   #TODO write Search Logic
   for u in ulist:
      p=u['firstName']+" "+u['lastName']+" "+u['bio']
      if search.lower() in p.lower():
         yield u

def evalWith(me,other):
   other=int(other)
   obj=Friend.objects.get(this_id=me)
   myfl=[ user[0] for user in obj.others.values_list()] 
   if(other in myfl):
      print(obj.others.remove(other))
      
   else:
      obj.others.add(other)

   myfl=[ user[0] for user in obj.others.values_list()]     
   print(myfl,sep='\n')

   return redirect('friends')
   
def getUserData(uidList):
   users=[]
   for uid in uidList:
      temp={'id':uid}
      user=User.objects.get(id=uid)
      temp['name']=user.firstName+" "+user.lastName
      details=Detail.objects.get(user=uid)
      temp['dp']=details.profilePicture
      users.append(temp)
   return users