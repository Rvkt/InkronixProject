from django.shortcuts import render
from courses.forms import Course_Form


# Create your views here.
def instructor_dashboard(request):
    return render(request, 'instructor/instructor-dashboard.html')


def instructor_add_course(request):
    form = Course_Form()
    context = {
        'form': form,
    }
    return render(request,'instructor/instructor-add-course.html', context)



def instructor_profile(request):
    return render (request, 'instructor/instructor-profile.html')


def instructor_reviews(request):
    return render (request, 'instructor/instructor-reviews.html')


def instructor_courses(request):
    return render (request, 'instructor/instructor-courses.html')


def instructor_announcements(request):
    return render (request, 'instructor/instructor-announcements.html')


def instructor_settings(request):
    return render (request, 'instructor/instructor-settings.html')


