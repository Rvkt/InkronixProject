from django.shortcuts import render

# Create your views here.
def student_dashboard(request):
    return render(request, 'student/student-dashboard.html')



def student_profile(request):
    return render (request, 'student/student-profile.html')


def student_reviews(request):
    return render (request, 'student/student-reviews.html')

def student_wishlist(request):
    return render (request, 'student/student-wishlist.html')


def student_enrolled_courses(request):
    return render (request, 'student/student-enrolled-courses.html')


def student_settings(request):
    return render (request, 'student/student-settings.html')

