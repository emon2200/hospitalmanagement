from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_appointment, name='create_appointment'),
    path('success/', views.success, name='success'),
    path('search/', views.search_appointment, name='sa'),  # Keep this
    path('appointment/<str:appointment_id>/', views.appointment_detail, name='appointment_detail'), # Change this
]