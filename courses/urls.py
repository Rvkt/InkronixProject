from django.urls import path
from .views import courses, courseDetails, courseList

urlpatterns = [
    path('', courses, name='courses'),
    path('course-list', courseList, name='course-list'),
    path('course-details', courseDetails, name='course-details'),
]
