from django.shortcuts import render

# Create your views here.
def studentDashboard(request):
    return render(request, 'student/student-dashboard.html')