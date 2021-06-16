from django.db import models
from phonenumber_field import modelfields
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    firstName=models.TextField(max_length=50)
    lastName=models.TextField(max_length=50)
    phNo=PhoneNumberField(blank=False, unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=64,default="")

    