from django.shortcuts import render
from rest_framework import generics,permissions
from .models import  Appointment, MoodEntry, ThoughtProcessing, PsychologicalDisorder
from .serializers import  AppointmentSerializer,AS, MoodEntrySerializer, ThoughtProcessingSerializer,PsychologicalDisorderSerializer,UserSerializer
from django.views import View
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.views import APIView
import urllib.parse
from django.utils import http
from django.contrib.auth import get_user_model
from social_core.backends import google


User = get_user_model()

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AppointmentShow(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AS

class AppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MoodEntryListCreateView(generics.ListCreateAPIView):
  
    serializer_class = MoodEntrySerializer
    def get_queryset(self):
        # Get the client_id from the request's query parameters or headers
        client_id = self.request.query_params.get('client_id')
        
        # Define the base queryset (all MoodEntry objects)
        queryset = MoodEntry.objects.all()

        # If client_id is provided, filter the queryset by client_id
        if client_id:
            queryset = queryset.filter(client_id=client_id)
        
        return queryset

class MoodEntryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer

class ThoughtProcessingListCreateView(generics.ListCreateAPIView):
    # queryset = ThoughtProcessing.objects.all()
    serializer_class = ThoughtProcessingSerializer
    
    def get_queryset(self):
        # Get the client_id from the request's query parameters or headers
        client_id = self.request.query_params.get('client_id')
        
        # Define the base queryset (all MoodEntry objects)
        queryset = ThoughtProcessing.objects.all()

        # If client_id is provided, filter the queryset by client_id
        if client_id:
            queryset = queryset.filter(client_id=client_id)
        return queryset
    
    
    
    
    

class ThoughtProcessingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ThoughtProcessing.objects.all()
    serializer_class = ThoughtProcessingSerializer
    
class PsychologicalDisorderListCreateView(generics.ListCreateAPIView):
    queryset = PsychologicalDisorder.objects.all()
    serializer_class = PsychologicalDisorderSerializer

class PsychologicalDisorderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PsychologicalDisorder.objects.all()
    serializer_class = PsychologicalDisorderSerializer

API_URL = 'https://5ce9-31-56-195-93.ngrok-free.app/auth/o/google-oauth2/'  
from social_core.backends import google


    

class RedirectSocial(APIView,google.GoogleOAuth2):
    STATE_PARAMETER = False
    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        return Response(json_obj)
        
#         s=requests.Session()
#         request.session['State']=state
#         print(request.session['State'])
#         request.session['google'] = state
#         request.session.save()
        

#         print(json_obj)
#         headers = {
#         # 'Cookie': f'session_state={request.session["oauth_state"]};',
#         'Content-Type': 'application/x-www-form-urlencoded',
# }

#         query_params = urllib.parse.urlencode(json_obj)
#         print(query_params)
#         form_data = {
#         'code': code,
#         'state': state,
#         'client_id': '855150297727-frj54btbp93i1g50tglt5klg7g1jvug6.apps.googleusercontent.com',
#         'client_secret': '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',
#         'redirect_uri': 'https://7bfb-31-56-195-93.ngrok-free.app/google',
#         'grant_type': 'authorization_code',
#         }

# # Make the POST request using the requests library
#         api_url = f"{API_URL}?{query_params}"
#         print(api_url)# Replace this with your actual API URL
#         response = requests.post(api_url ,data=form_data, headers=headers)
#         print(response.text)

#         # Assuming the response contains the data you need
        
        
#         # Return the JSON object as the response to the GET request
#         return Response(json_obj)
        # details = {
        #     'state': state,
        #     'code': code,
        #     # 'client_id': '855150297727-frj54btbp93i1g50tglt5klg7g1jvug6.apps.googleusercontent.com',
        #     # 'client_secret': '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',
        #     # 'redirect_uri': 'https://7bfb-31-56-195-93.ngrok-free.app/auth/o/google-oauth2/',
        #     # 'grant_type': 'authorization_code',  # Fixed: Add quotes to 'authorization_code'
        # }

        
        

        # Making the POST request to the specified URL
        
        