from django.urls import path
from . import views

urlpatterns = [

    # Edited by Ravi Kant
    path('', views.instructor, name='instructor'),
    path('dashboard', views.instructor_dashboard, name='instructor_dashboard'),
    path('profile', views.instructor_profile, name='instructor_profile'),
    path('enrolled-courses', views.instructor_enrolled_courses, name='instructor_enrolled_courses'),
    path('wishlist', views.instructor_wishlist, name='instructor_wishlist'),
    path('reviews', views.instructor_reviews, name='instructor_reviews'),
    path('my-quiz-attempts', views.instructor_my_quiz_attempts, name='instructor_my_quiz_attempts'),
    path('order-history', views.instructor_order_history, name='instructor_order_history'),
    path('courses', views.instructor_courses, name='instructor_courses'),
    path('announcements', views.instructor_announcements, name='instructor_announcements'),
    path('quiz-attempts', views.instructor_quiz_attempts, name='instructor_quiz_attempts'),
    path('assignments', views.instructor_assignments, name='instructor_assignments'),
    path('settings', views.instructor_settings, name='instructor_settings'),


]