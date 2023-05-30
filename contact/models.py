from django.db import models


# Create your models here.
class contactDetail(models.Model):  
    name= models.CharField(max_length=20)  
    email= models.CharField(max_length=30)  
    number = models.IntegerField()  
    message  = models.TextField()  
   