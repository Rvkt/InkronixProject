# from django.urls import path
# from .views import loginUser, registerUser

# urlpatterns = [
#     path('login', loginUser, name='login'),
#     path('register', registerUser, name='register'),
# ]



from django.urls import path
from . import views

urlpatterns=[
     path('register',views.register_user, name='register'),
     
     path('student_register',views.student_register.as_view(), name='student_register'),
     path('instructor_register',views.instructor_register.as_view(), name='instructor_register'),

     path('login',views.login_user, name='login'),
     path('logout',views.logout_user, name='logout'),
]