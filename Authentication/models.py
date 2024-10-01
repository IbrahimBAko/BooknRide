from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#This is a user model for creating login details!!

class User(AbstractUser):
    username = models.CharField(unique=True, max_length= 50)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    #This is a model for creating user profile details!!

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=70)
    Middle_Name = models.CharField(max_length=70)
    Last_Name = models.CharField(max_length=70)
    Profile_Picture = models.ImageField(upload_to='userfolder/profile_pictures', blank=True,null=True)
    Cover_Photo = models.ImageField(upload_to='userfolder/cover_photos', blank=True, null=True)
    DOB = models.DateTimeField(auto_now_add=False, blank=False, null=False)
    Address_Line1 = models.CharField(max_length=150)
    Address_Line2 = models.CharField(max_length=150)
    Nationality = models.CharField(max_length=100, blank=False, null=False)
    City = models.CharField(max_length=70, null=False, blank=False)
    Zip_or_Postcode = models.CharField(max_length=50, blank=False, null=False)
    Mobile_Number = models.CharField(max_length=50, blank=False, null=False)
    Created_At = models.DateTimeField(auto_now_add=True)
    Modified_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.First_Name
    






























