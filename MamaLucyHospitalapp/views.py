from django.shortcuts import render,redirect
from MamaLucyHospitalapp.models import Appointment

def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')

def appointment(request):
    if request.method == 'POST':
        appointments= Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        appointments.save()
        return redirect("/appointment")
    else:
        return render(request, 'appointment.html')
# Create your views here.
