from django.shortcuts import render
from .models import License, Service, Statistic

def home(request):
    return render(request, 'home.html')

def team(request):
    return render(request, 'team.html')

def statistics_view(request):
    return render(request, 'statistics.html')

def feature(request):
    return render(request, 'feature.html')

def contact(request):
    return render(request, 'contact.html')

def appointment(request):
    return render(request, 'appointment.html')

def application(request):
    return render(request, 'application.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')
