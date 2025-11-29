from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, UserRegistrationView
from doctors.views import  DoctorViewSet


router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'userregis', UserRegistrationView)


urlpatterns = [
      path('', include(router.urls)),
    path('create/', views.create_appointment, name='create_appointment'),
    path('success/', views.success, name='success'),
    path('search/', views.search_appointment, name='sa'),  # Keep this
    path('appointment/<str:appointment_id>/', views.appointment_detail, name='appointment_detail'), # Change this
]