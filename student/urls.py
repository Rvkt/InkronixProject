from django.urls import path
from .views import studentDashboard

urlpatterns = [
    path('', studentDashboard, name='student')
]
