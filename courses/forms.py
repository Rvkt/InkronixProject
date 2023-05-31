from django.forms import ModelForm
from django import forms
from .models import Course


class Course_Form(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def save(self):
        course = super().save(commit=False)
        course.save()
        return course




