from django.shortcuts import render
from .models import Doctor


# Create your views here.


def doctors_list(request):
    doctors = Doctor.objects.all()  # Fetch all doctors
    return render(request, 'doctors.html', {'doctors': doctors})

# doctors/views.py
from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
