from django.urls import path
from . import views

urlpatterns = [
    path('', views.Course, name='Course'),
]