from django.shortcuts import render

# Create your views here.
def courses(request):
    return render(request, 'courses/courses.html')


def courseDetails(request):
    return render(request, 'courses/course-details.html')


def courseList(request):
    return render(request, 'courses/course-list.html')