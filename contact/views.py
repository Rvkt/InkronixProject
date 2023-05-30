from django.shortcuts import render
from contact.models import contactDetail


# Create your views here.
def contact(request):
    msg=""
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        message=request.POST.get('message')
        
        en=contactDetail(name=name,email=email,number=number,message=message)
        en.save()
        msg="Data inserted"
    return render(request, 'Contact/contact.html',{'msg':msg})