from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


# def contact(request):
#     return render(request, 'home/contact.html')


def allcategory(request):
    return render(request, 'home/allcategory.html')


def about(request):
    return render(request, 'home/about.html')


def testing(request):
    return render(request, 'home/testing.html')