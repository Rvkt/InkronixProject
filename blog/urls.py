from django.urls import path
from blog import views
from blog.views import BlogView, BlogAV, BlogDetailAV, WriterAV#, PaginatedListView#BlogFormView
# from django.conf.urls import url

urlpatterns = [
    path('', views.bloghome, name='blog'),
    # path('blog-form', BlogFormView.as_view(), name='blog-form'),
    # path('blog-form', BlogCreate.as_view()),
    path('blog-form', views.BlogFormView, name='blog-form'),
    path('<int:pk>', BlogView.as_view(), name='blog-page'),
    path('blog-view', BlogAV.as_view(), name='blog-view'),
    path('blog-view/<int:pk>', BlogDetailAV.as_view(), name='blog-detail'),
    path('writer', WriterAV.as_view(), name='writer'),
    # path('search-view/', BlogSearchView.as_view(), name="search-view")
]

# WARNINGS:
# ?: (2_0.W001) Your URL pattern '^blog-search-result/$' [name='blog-search-result'] has a route that
# contains '(?P<', begins with a '^', or ends with a '$'. This was likely an oversight when migrating to django.urls.path().

# this new admin url is awesome: http://127.0.0.1:8019/admin/blog/
