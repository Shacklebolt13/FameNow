from django.http import HttpRequest
from django.shortcuts import render

def sortQ(ulist:list,search:str):
   #TODO write Search Logic
   for u in ulist:
      p=u['firstName']+" "+u['lastName']+" "+u['bio']
      print(p)
      if search.lower() in p.lower():
         yield u
