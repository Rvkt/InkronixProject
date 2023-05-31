from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('contact/', include('contact.urls')),
    path('', include('home.urls')),
    path('instructor/', include('instructor.urls')),
    path('student/', include('student.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
