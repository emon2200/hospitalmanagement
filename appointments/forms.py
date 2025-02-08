from django import forms
from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patient

class AppointmentForm(forms.ModelForm):
    name = forms.CharField(
        label="name",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter patient name'}),
    )
    phone = forms.CharField(
        label="phone",
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
    )
    class Meta:
        model = Appointment
        fields = ['name','phone', 'doctor', 'appointment_date', 'appointment_time', 'reason']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

  
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        label="Doctor Category",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
