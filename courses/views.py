from django.shortcuts import render
from django.views.generic import CreateView

from django.shortcuts import redirect

from .forms import Course_Form
from .models import Course


# Create your views here.
def courses(request):

    courses = Course.objects.all().order_by('-created_on')[0:]

    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)



class course_added(CreateView):
    model = Course()
    form_class = Course_Form
    template_name = 'instructor/instructor-add-course.html'

    def form_valid(self, form):
        course = form.save()
        return redirect('courses')





def courseDetails(request):
    return render(request, 'courses/course-details.html')


def courseList(request):
    return render(request, 'courses/course-list.html')