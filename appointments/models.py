from django.db import models
# Import statements for models
from doctors.models import Doctor  # Correct import for Doctor model
from patients.models import Patient  # Correct import for Patient model


class Appointment(models.Model):
    appointment_id = models.CharField(max_length=30, unique=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField() 
    email=models.EmailField()

    def save(self, *args, **kwargs):
        if not self.appointment_id:
            date_part = self.appointment_date.strftime("%d%m%y")
            doctor_part = "_".join(self.doctor.doctor_id.split("_")[1:3])
            patient_part = self.patient.patient_id.split("_")[1]
            self.appointment_id = f"{date_part}_{doctor_part}_{patient_part}"
        super(Appointment, self).save(*args, **kwargs)

    def __str__(self):
        return f"Appointment with {self.doctor.name} on {self.appointment_date}"
# models.py
from django.db import models

class UserRegistration(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Hash করবেন পরে
    gender = models.CharField(max_length=10)
    op = models.BooleanField(default=False)

    def __str__(self):
        return self.fname
