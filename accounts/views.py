from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import Student_SignUp_Form, Instructor_SignUp_Form
from django.contrib.auth.forms import AuthenticationForm
from .models import User

# Create your views here.

def register_user(request):
    return render(request, 'accounts/register.html')


class student_register(CreateView):
    model = User
    form_class = Student_SignUp_Form
    template_name = 'accounts/student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student')


class instructor_register(CreateView):
    model = User
    form_class = Instructor_SignUp_Form
    template_name = 'accounts/instructor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('instructor')


# def loginUser(request):
#     return render(request, 'accounts/login.html')



def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)

                # Check for the user type
                if user.is_student:
                    print(f'Student : {user.first_name}')
                    return redirect('student')
                elif user.is_instructor:
                    print(f'Instructor: {user.first_name}')
                    return redirect('instructor')
                else:
                    return redirect('/admin')
                
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")

    return render(request, 'accounts/login.html', context={'form':AuthenticationForm()})



def logout_user(request):
    logout(request)
    return redirect('/')