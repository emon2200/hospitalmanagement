from django.urls import path
from . import views
# doctors/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create', views.doctors_list, name='doctors'),  # List of doctors
]