from django.shortcuts import render

# Create your views here.


# Edited by Ravi Kant
# views to render the instructor templates
def instructor(request):
    return render(request, 'instructor/instructor.html')

def instructor_dashboard(request):
    return render(request, 'instructor/instructor-dashboard.html')

def instructor_profile(request):
    return render(request, 'instructor/instructor-profile.html')

def instructor_enrolled_courses(request):
    return render(request, 'instructor/instructor-enrolled-courses.html')

def instructor_wishlist(request):
    return render(request, 'instructor/instructor-wishlist.html')

def instructor_reviews(request):
    return render(request, 'instructor/instructor-reviews.html')

def instructor_my_quiz_attempts(request):
    return render(request, 'instructor/instructor-my-quiz-attempts.html')

def instructor_order_history(request):
    return render(request, 'instructor/instructor-order-history.html')

def instructor_courses(request):
    return render(request, 'instructor/instructor-courses.html')

def instructor_announcements(request):
    return render(request, 'instructor/instructor-announcements.html')

def instructor_quiz_attempts(request):
    return render(request, 'instructor/instructor-quiz-attempts.html')

def instructor_assignments(request):
    return render(request, 'instructor/instructor-assignments.html')

def instructor_settings(request):
    return render(request, 'instructor/instructor-settings.html')