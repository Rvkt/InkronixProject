from django.db import models
from accounts.models import Instructor

# Create your models here.
class Course(models.Model):
    author          = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title           = models.CharField(max_length=255)
    image           = models.ImageField(upload_to='images/courses')
    
    price = models.IntegerField()
    
    language        = models.CharField(max_length=50)
    category        = models.CharField(max_length=100)
    short_intro     = models.CharField(max_length=50)
    description     = models.TextField()

    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    