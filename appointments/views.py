from django.shortcuts import render, redirect,get_object_or_404
from appointments.models import Appointment
from patients.models import Patient
from .forms import AppointmentForm
from django.core.mail import send_mail

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email=form.cleaned_data['email']
           

            # Check if patient already exists
            patient, created = Patient.objects.get_or_create(
                phone=phone,
                name=name
            )
            appointment = form.save(commit=False)  # Do not save to the database yet
            appointment.patient = patient  # Set the patient relationship
            appointment.save()  # Now save to the database
            if email:
                send_mail(
                    subject="আপনার অ্যাপয়েন্টমেন্ট নিশ্চিতকরণ",
                    message=f"প্রিয় {name},\n\nআপনার অ্যাপয়েন্টমেন্ট সফলভাবে বুক করা হয়েছে।\nঅ্যাপয়েন্টমেন্ট আইডি:{appointment.appointment_id}\n\nধন্যবাদ!",
                    from_email="procyonemon@gmail.com",
                    recipient_list=[email],
                    fail_silently=False,
                )

            return redirect('success')  
    else:
        form = AppointmentForm()
    
    return render(request, 'create_appointment.html', {'form': form})
def success(request):
    return render(request, 'success.html')
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Appointment  # Import your model

def search_appointment(request):
    appointment_id = request.GET.get('appointment_id', '').strip()
    if appointment_id:
        try:
            appointment = get_object_or_404(Appointment, appointment_id=appointment_id) # get the object or 404
            return redirect('appointment_detail', appointment_id=appointment.appointment_id)
        except Appointment.DoesNotExist:
            messages.error(request, "Appointment not found.")
            return render(request, 'sa.html')
    return render(request, 'sa.html') # if no id given just render the search page

def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
    return render(request, 'appointment_detail.html', {'appointment': appointment})

from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
# views.py
from rest_framework import generics
from .models import UserRegistration
from .serializers import UserRegistrationSerializer

class UserRegistrationView(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer
