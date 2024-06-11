from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('team/', views.team, name='team'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('feature/', views.feature, name='feature'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('application/', views.application, name='application'),
    path('check-coordinates/', views.check_coordinates, name='check_coordinates'),
    path('request-token/', views.request_token, name='request_token'),
    path('upload-pdf/', views.upload_pdf, name='upload_pdf'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('success/', views.contact_success, name='contact_success'),
    path('appointment-success/', views.appointment_success, name='appointment_success'),

]
