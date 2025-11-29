from django.db import models

class Doctor(models.Model):
    CATEGORY_CHOICES = [
        ('Heart', 'Heart Specialist'),
        ('Liver', 'Liver Specialist'),
        ('Skin', 'Dermatologist'),
        ('child and newborn', 'Pediatrician'),
    ]

    doctor_id = models.CharField(max_length=20, unique=True, blank=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    phone = models.CharField(max_length=15)
    time=models.CharField(max_length=15)
    
    def save(self, *args, **kwargs):
        if not self.doctor_id:
            category_code = self.category[:3].upper()
            unique_number = str(Doctor.objects.filter(category=self.category).count() + 1).zfill(3)
            self.doctor_id = f"D_{category_code}_{unique_number}"
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
