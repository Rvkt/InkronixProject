from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def accounts(request):
    # return HttpResponse('Accounts page')
    return render(request, 'dashboard.html')
