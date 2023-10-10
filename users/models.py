from django.db import models
from . manager import UserManager
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

# ----------------------------------------------------- Here we are creating the custome user model -----------------------------------------------
class CustomUser(AbstractUser):

    GENDER_CHOICES = (
        ("male", 'Male'),
        ("female", 'Female'),
        ("others", 'Others')
    )

    username = None
    #id = models.IntegerField(auto_created=True)
    first_name = models.CharField(verbose_name="First Name",  max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Last Name")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default= "Male")
    age = models.IntegerField(verbose_name="Age",)
    email = models.EmailField(max_length=128, unique=True, verbose_name="Email", primary_key=True)
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name="Address", )
    pincode = models.IntegerField( null=True, blank=True, verbose_name="Pin Code")


    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'gender', 'age']

    objects = UserManager()

    def __str__(self):
        return self.email
    


#-------------------------------------------------------------------------------------------------------------------------------------