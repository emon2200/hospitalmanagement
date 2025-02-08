from django.shortcuts import render, redirect,get_object_or_404
from appointments.models import Appointment
from patients.models import Patient
from .forms import AppointmentForm

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            # Check if patient already exists
            patient, created = Patient.objects.get_or_create(
                phone=phone,
                name=name
            )
            appointment = form.save(commit=False)  # Do not save to the database yet
            appointment.patient = patient  # Set the patient relationship
            appointment.save()  # Now save to the database
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