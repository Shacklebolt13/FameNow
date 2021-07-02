from django.db import models
from phonenumber_field import modelfields
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    email=models.EmailField(blank=False,unique=True)
    password=models.CharField(max_length=64,default="")
    firstName=models.TextField(max_length=50)
    lastName=models.TextField(max_length=50)
    phNo=PhoneNumberField()
    gender=models.BooleanField()
    
    def __str__(self):
        return f"{self.id} {self.firstName} {self.lastName}" 

class Detail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profilePicture=models.ImageField(upload_to="images/useruploads")
    bio=models.TextField(max_length=250)
    def __str__(self):
        return f"{self.user.id} details" 
    