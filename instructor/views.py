from django.shortcuts import render

# Create your views here.
def instructorDashboard(request):
    return render(request, 'instructor/instructor-dashboard.html')