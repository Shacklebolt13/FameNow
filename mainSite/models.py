from django.db import models
from phonenumber_field import modelfields
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    firstName=models.TextField(max_length=50)
    lastName=models.TextField(max_length=50)
    phNo=PhoneNumberField(unique=True)
    email=models.EmailField(blank=False,unique=True)
    password=models.CharField(max_length=64,default="")
    gender=models.BooleanField()
    profilePicture=models.ImageField(upload_to="images/useruploads")
    
    def __str__(self):
        return f"{self.id} {self.firstName} {self.lastName}" 

    def create(firstName,lastName,phNo,email,password,gender,profilePicture,self) -> None:
        data={
            "firstName":firstName,
            "lastName":lastName,
            "phNo":phNo,
            "password":password,
            "gender":gender,
            "email":email,
            "profilePicture":profilePicture
        }
        super().__init__(kwargs=data)