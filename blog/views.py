from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'Blog/blog.html')


def blogPage(request):
    return render(request, 'Blog/blog-page.html')