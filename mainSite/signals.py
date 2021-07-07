from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User,Detail

@receiver(post_save,sender=User)
def CreateUser(instance: User,created,**kwargs):
    if(created):
        if(instance.gender):
            dp="images/defaultMan.png"
        else:
            dp="images/defaultWoman.png"
    
        Detail(user=instance,profilePicture=dp,bio="THIS IS MY BIO").save()
