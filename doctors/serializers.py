# doctors/serializers.py
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctor_id', 'name', 'category', 'phone', 'time']
        fields = '__all__'   # doctor_id auto generate
