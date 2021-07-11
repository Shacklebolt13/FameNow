from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Friend, User,Detail

@receiver(post_save,sender=User)    #DETAIL 
def CreateUser(instance: User,created,**kwargs):
    if(created):
        if(instance.gender):
            dp="images/defaultMan.png"
        else:
            dp="images/defaultWoman.png"
    
        Detail(user=instance,profilePicture=dp,bio="THIS IS MY BIO").save()


@receiver(post_save,sender=Detail)    #FRIENDS
def CreateFriends(instance: Detail,created,**kwargs):
    if(created):
        Friend(this=instance).save()
