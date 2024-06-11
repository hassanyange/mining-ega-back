from django.shortcuts import render, redirect
from .models import License, Service, Statistic
from .forms import ContactForm, AppointmentForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authtoken.models import Token  
from .models import Coordinate, Token, Application
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm
import random
import string


def home(request):
    form = AppointmentForm()
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
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Redirect to a success page
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})


def appointment_success(request):
    return render(request, 'appointment_success.html')




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('application')  # Redirect to the application page
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def application(request):
    return render(request, 'application.html')


@login_required
def check_coordinates(request):
    if request.method == 'POST':
        coordinates = request.POST.get('coordinates')
        if Coordinate.objects.filter(coordinates=coordinates).exists():
            return JsonResponse({'available': False})
        else:
            return JsonResponse({'available': True})
        


@login_required
def request_token(request):
    if request.method == 'POST':
        user = request.user
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Token does not exist for this user.'}, status=400)

        user_email = user.email  # Access the user's email address
        token_str = token.token  # Access the token value from your custom Token model
        send_mail(
            'Your Access Token',
            f'Your token is: {token_str}',
            settings.DEFAULT_FROM_EMAIL,
            [user_email],  # Use the user's email address as the recipient
            fail_silently=False,
        )
        return JsonResponse({'token_requested': True, 'message': 'Token has been sent to your email.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'})



@login_required
def upload_pdf(request):
    if request.method == 'POST':
        token_str = request.POST.get('token')
        coordinates = request.POST.get('coordinates')
        user = request.user
        email = request.POST.get('email')
        try:
            token = Token.objects.get(token=token_str, user=user)
            pdf_file = request.FILES['pdfFile']
            Application.objects.create(user=user, email=email, coordinates=coordinates, pdf_file=pdf_file)
            return JsonResponse({'upload_success': True})
        except Token.DoesNotExist:
            return JsonResponse({'upload_success': False})

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')
