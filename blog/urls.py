from django.urls import path
from .views import blogPage, blog

urlpatterns = [
    path('', blog, name='blog'),
    path('blogpage', blogPage, name='blogpage')
]
