from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class HealthPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    national_ID=models.CharField(max_length =16)
    health_Post_Name=models.CharField(max_length =50)
    district_Name=models.CharField(max_length =20)
    health_Facility_Type=models.CharField(max_length =30)

    def __str__(self):
        return self.hpost_name

    # @classmethod
    # def get_picture(cls,id):
    #     Profile.objects.all()

class WelcomeMsgRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Patient(models.Model):
   
    household_ID=models.CharField(max_length =16)
    application_ID=models.CharField(max_length =8)
    household_Name=models.CharField(max_length =50)
    ubudehe_Category = models.IntegerField(choices=list(zip(range(1, 5), range(1, 5))))
    beneficiary_Name=models.CharField(max_length =50)
    phone_Number=models.CharField(max_length =60)
    dOB=models.CharField(max_length =4)
    sex=models.CharField(max_length =30)
    prisonner=models.CharField(max_length =3)
    catchement_Area=models.CharField(max_length =60)
#     def save_projects(self):
#         self.save() 
    
#     @classmethod
#     def get_pic(cls,id):
#         Projects.objects.all()

#     @classmethod
#     def count_posts(cls,id):
#         Projects.objects.all().count()

#     def __str__(self):
#         return self.title
    
#     @classmethod
#     def search_by_title(cls,search_term):
#         images=Projects.objects.filter(title__icontains=search_term)
#         return images 


class ServiceDetails(models.Model):
   
    type_Of_Medical_Visit=models.CharField(max_length =15)
    desease_Episode=models.CharField(max_length =15)
    purpose_Of_The_Visit=models.CharField(max_length =15)
    consultation=models.CharField(max_length =100)
   

#     @classmethod
#     def get_rates(cls,id):
#         Rating2.objects.all()
        

#     def save_rates2(self):
#         self.save() 
