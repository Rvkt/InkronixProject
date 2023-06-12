from django.urls import path
from . import views



urlpatterns = [
    path('', views.instructor_dashboard, name='instructor'),
    path('create-new-course', views.instructor_add_course, name='instructor_add_course'),
    path('profile', views.instructor_profile, name='instructor_profile'),
    path('reviews', views.instructor_reviews, name='instructor_reviews'),
    path('courses', views.instructor_courses, name='instructor_courses'),
    path('announcements', views.instructor_announcements, name='instructor_announcements'),
    path('settings', views.instructor_settings, name='instructor_settings'),
]




