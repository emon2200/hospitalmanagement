import datetime
from django.db import models
class Patient(models.Model):
    patient_id = models.CharField(max_length=20, unique=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
  
    def save(self, *args, **kwargs):
        if not self.patient_id:
            unique_number = str(Patient.objects.count() + 1).zfill(4)
            self.patient_id = f"P_{unique_number}"
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
