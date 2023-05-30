from django.urls import path
from .views import instructorDashboard

urlpatterns = [
    path('', instructorDashboard, name='instructor')
]
