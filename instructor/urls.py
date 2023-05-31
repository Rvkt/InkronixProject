from django.urls import path
from .views import instructorDashboard, instructor_add_course

urlpatterns = [
    path('', instructorDashboard, name='instructor'),
    path('create-new-course', instructor_add_course, name='instructor_add_course'),
]
