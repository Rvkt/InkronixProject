from django.db import models
from accounts.models import Instructor, Student

# Create your models here.
class Course(models.Model):
    author          = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    student         = models.ManyToManyField(Student)
    title           = models.CharField(max_length=255)
    image           = models.ImageField(upload_to='images/courses')
    
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    off_price = models.IntegerField(default=0)

    language        = models.CharField(max_length=50)

    COURSE_CATEGORY = (
        ("app-web-development", "App & Web Development"),
        ("digital-marketing", "Digital Marketing"),
        ("graphics-designing", "Graphics Designing"),
        ("python-programming", "Python Programming"),
        ("artificial-intelligence", "Artificial Intelligence"),
        ("government-exams", "Government Exams"),
    )

    # category        = models.CharField(max_length=100)
    category        = models.CharField(max_length=100, choices = COURSE_CATEGORY, default = 'app-web-development' )

    short_intro     = models.CharField(max_length=50)
    description     = models.TextField()

    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    