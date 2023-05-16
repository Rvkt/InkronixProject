from django.shortcuts import render


# Create your views here.


def Blog(request):
    return render(request, 'Blogs/blog.html')
