from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class MoodEntry(models.Model):
   

    mood_overall = models.CharField(max_length=10)
    mood_specific = models.CharField(max_length=100)
    mood_cause = models.CharField(max_length=100)
    mood_journal = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

class Appointment(models.Model):
    

    Problem = models.CharField(max_length=100)

    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey(User, on_delete=models.CASCADE,default=1)    
    # Add other fields as needed
class ThoughtProcessing(models.Model):
    

    thought_negative = models.CharField(max_length=100)
    thought_distortion = models.CharField(max_length=100)
    thought_challenge = models.TextField()
    thought_alternative = models.TextField()
    # feeling = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey(User, on_delete=models.CASCADE,default=1)


    # Add other fields as needed

class PsychologicalDisorder(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=10)
    client = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

