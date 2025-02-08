from django.shortcuts import render
from .models import Doctor


# Create your views here.


def doctors_list(request):
    doctors = Doctor.objects.all()  # Fetch all doctors
    return render(request, 'doctors.html', {'doctors': doctors})