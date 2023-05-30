from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('contact/', include('contact.urls')),
    path('', include('home.urls')),
    path('instructor/', include('instructor.urls')),
    path('student/', include('student.urls')),
]
