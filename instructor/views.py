from django.shortcuts import render
from courses.forms import Course_Form


# Create your views here.
def instructorDashboard(request):
    return render(request, 'instructor/instructor-dashboard.html')


def instructor_add_course(request):

    form = Course_Form()

    context = {
        'form': form,
    }
    
    return render(request,'instructor/instructor-add-course.html', context)