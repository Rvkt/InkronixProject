from django.shortcuts import render

# Create your views here.
def student_dashboard(request):
    return render(request, 'Student/student-dashboard.html')

def student_profile(request):
    return render(request, 'Student/student-profile.html')

def student_enrolled_courses(request):
    return render(request, 'Student/student-enrolled-courses.html')

def student_wishlist(request):
    return render(request, 'Student/student-wishlist.html')

def student_reviews(request):
    return render(request, 'Student/student-reviews.html')

def student_my_quiz_attempts(request):
    return render(request, 'Student/student-my-quiz-attempts.html')

def student_order_history(request):
    return render(request, 'Student/student-order-history.html')

def student_settings(request):
    return render(request, 'Student/student-settings.html')











