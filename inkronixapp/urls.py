from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('allCategory/', views.allCategory, name='allCategory'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('login/',views.login,name="login"),
    path('signup/',views.registration,name="signup"),


]
