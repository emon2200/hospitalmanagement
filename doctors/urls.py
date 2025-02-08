from django.urls import path
from . import views

urlpatterns = [
    path('create', views.doctors_list, name='doctors'),  # List of doctors
]