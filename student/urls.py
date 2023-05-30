from django.urls import path
from .views import *

urlpatterns = [
    path('', student_dashboard, name='student'),
    path('student-profile', student_profile, name='student_profile'),
    path('student-enrolled-courses', student_enrolled_courses, name='student_enrolled_courses'),
    path('student-wishlist', student_wishlist, name='student_wishlist'),
    path('student-reviews', student_reviews, name='student_reviews'),
    path('student-my-quiz-attempts', student_my_quiz_attempts, name='student_my_quiz_attempts'),
    path('student-order-history', student_order_history, name='student_order_history'),
    path('student-settings', student_settings, name='student_settings'),
]