from django.urls import path
from .views import courses, courseDetails, courseList, course_added

urlpatterns = [
    path('', courses, name='courses'),
    path('course-list', courseList, name='course-list'),
    path('course-details', courseDetails, name='course-details'),
    path('course-added', course_added.as_view(), name='course_added'),
]
