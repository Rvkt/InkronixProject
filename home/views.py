from django.shortcuts import render
from courses.models import Course


# Create your views here.
def index(request):

    courses = Course.objects.all().order_by('-created_on')[:6]

    context = {
        'courses': courses
    }

    return render(request, 'home/index.html', context)


# def contact(request):
#     return render(request, 'home/contact.html')


def allcategory(request):
    return render(request, 'home/allcategory.html')


def about(request):
    return render(request, 'home/about.html')


def testing(request):
    return render(request, 'home/testing.html')