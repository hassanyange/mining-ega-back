from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('feature/', views.feature, name='feature'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('application/', views.application, name='application'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
]
