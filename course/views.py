from django.shortcuts import render


# Create your views here.

def Course(request):
    return render(request, 'Course/courses.html')
