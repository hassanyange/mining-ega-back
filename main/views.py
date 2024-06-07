from django.shortcuts import render, redirect
from .models import License, Service, Statistic
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')

def team(request):
    return render(request, 'team.html')

def statistics_view(request):
    return render(request, 'statistics.html')

def feature(request):
    return render(request, 'feature.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def appointment(request):
    return render(request, 'appointment.html')

def application(request):
    return render(request, 'application.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')
