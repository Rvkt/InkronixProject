from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_dashboard, name='student'),
    path('profile', views.student_profile, name='student_profile'),
    path('enrolled-courses', views.student_enrolled_courses, name='student_enrolled_courses'),
    path('wishlist', views.student_wishlist, name='student_wishlist'),
    path('reviews', views.student_reviews, name='student_reviews'),
    path('settings', views.student_settings, name='student_settings'),
]
