from django.urls import path
from .views import index, about, allcategory

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    # path('contact', contact, name='contact'),
    path('allcategory', allcategory, name='allcategory'),

]
