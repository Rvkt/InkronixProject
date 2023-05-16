
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog',include('blog.urls')),
    path('course',include('course.urls')),
    path('account', include("accounts.urls")),
    path('', include("inkronixapp.urls"))
]
