from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Home/index.html')


# def contact(request):
#     return render(request, 'home/contact.html')


def allcategory(request):
    return render(request, 'Home/allcategory.html')


def about(request):
    return render(request, 'Home/about.html')


def testing(request):
    return render(request, 'Home/testing.html')
