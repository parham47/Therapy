from rest_framework import serializers
from .models import  Appointment, MoodEntry, ThoughtProcessing,PsychologicalDisorder
from django.contrib.auth import get_user_model

User = get_user_model()
class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = '__all__'
        depth = 2
class AS(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = '__all__'
  

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = '__all__'

class ThoughtProcessingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThoughtProcessing
        fields = '__all__'
        
class PsychologicalDisorderSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PsychologicalDisorder
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = '__all__'