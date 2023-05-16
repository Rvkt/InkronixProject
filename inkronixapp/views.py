from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Home page')
    return render(request, 'Inkronixapp/index.html')


def about(request):
    return render(request, 'Inkronixapp/about.html')


def allCategory(request):
    return render(request, 'Inkronixapp/allCategory.html')


def contact(request):
    return render(request, 'Inkronixapp/contact.html')


def blog(request):
    return render(request, 'Blogs/blog.html')




# --------------- Vedant 2023_05_16 18:34 -------------------------------------------



def login(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user:
            flag=check_password(request, Password,user.password)

            if user.is_superuser:
                return redirect('/admin') # replace 'admin_home' with the name of your admin home page URL
            else:
                return redirect('/') # replace 'home' with the name of your home page URL
        else:
            error_message = "Invalid email or password."
            return render(request, 'inkronixapp/login.html', {'error_message': error_message})
    else:
        return render(request, 'inkronixapp/login.html')
    

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('') # replace 'home' with the name of your home page URL
        except:
            messages.error(request, "Error creating user account")
            return redirect('login')
    else:
        
        return render(request,'inkronixapp/registration.html')



# ----------------------------------------------------------------------------------------------
# (NOT WORKING)
# def login(request):
#     # if request.method == 'GET':
#     #     return render(request,'inkronixapp/login.html')
#     if request.method=="POST":

#         Username = request.POST.get('username')
#         Password = request.POST.get('password')
#         user = authenticate(request, username=Username, password=Password)
#         User1=Userlogin.get_User_by_password(Password)

#         if user:
#             flag=check_password(request, Password,user.password)

#             if user.is_superuser:
#                 return redirect('/admin') # replace 'admin_home' with the name of your admin home page URL
#             else:
#                 return redirect('/') # replace 'home' with the name of your home page URL
#         else:
#             error_message = "Invalid email or password."
#             return render(request, 'inkronixapp/login.html', {'error_message': error_message})
#     else:
#         return render(request, 'inkronixapp/login.html')
    

# def registration(request):
#     data={}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match")
#             return redirect('signup')

#         else:
#             data['username']=username
#             data['email']=email
#             data['password']=confirm_password

#             User1=Userlogin(username=username,email=email,password=confirm_password)

#             User1.save()

#             user=authenticate(username=username,password=confirm_password)
#             if user is not None:
#                 login(request,user)
#             else:
#                 messages.error(request,"Invalid username or password!")
#                 return redirect('login')
#     else:
#         return render(request,'inkronixapp/registration.html')       
    