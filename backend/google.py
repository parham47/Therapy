from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

API_URL = 'https://db83-151-241-18-241.ngrok-free.app'

class GoogleOauthAPIView(APIView):
 from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt  # Only use csrf_exempt if you are sure about the security implications
def google_callback_view(request):
    if request.method == 'GET':
        # Retrieve the code and state parameters from the callback URL
        code = request.GET.get('code')
        state = request.GET.get('state')

        # Perform any necessary processing with 'code' and 'state'
        # (e.g., save to session, verify state, etc.)

        # Make a POST request to Djoser social auth URL
        djoser_social_auth_url = 'https://your-djoser-social-auth-url/'  # Replace with actual URL
        response = requests.post(djoser_social_auth_url, data={'code': code})

        # Handle the response from Djoser



        if not code or not state:
            # If 'code' or 'state' parameters are missing, return an error response
            return Response({"error": "Missing 'code' or 'state' parameters"}, status=status.HTTP_400_BAD_REQUEST)

        # Fixed: Use 'authorization_code' as a string, not an undefined variable
        details = {
            'state': state,
            'code': code,
            'client_id': '855150297727-frj54btbp93i1g50tglt5klg7g1jvug6.apps.googleusercontent.com',
            'client_secret': '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',
            'redirect_uri': 'https://3ccb-151-241-18-241.ngrok-free.app/auth/o/google-oauth2/',
            'grant_type': 'authorization_code',  # Fixed: Add quotes to 'authorization_code'
        }

        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        # Making the POST request to the specified URL
        # Fixed: Replace 'YOUR_API_URL' with the actual URL
        response = requests.post(API_URL, data=details, headers=header)  # Fixed: Add 'data' parameter to send details

        # Assuming the response contains the data you need
        response_data = response.json()

        # Now you can process the response data as needed
        print(response_data)

        if response.status_code != status.HTTP_200_OK:
            # If Google OAuth returns an error, return the error response
            return Response(response.json(), status=response.status_code)

        # Successfully received the access token
        access_token = response.json().get('access_token')

        # Use the access token to fetch user data from Google
        google_user_info_url = f'https://www.googleapis.com/oauth2/v3/userinfo?access_token={access_token}'

        user_info_response = requests.get(google_user_info_url)

        if user_info_response.status_code != status.HTTP_200_OK:
            # If fetching user data fails, return an error response
            return Response(user_info_response.json(), status=user_info_response.status_code)

        # Successfully fetched user data from Google
        user_data = user_info_response.json()

        # Now, you can send the user data to your React Native app and navigate to the home screen
        # For example, you can return the user data as a JSON response
        return Response(user_data, status=status.HTTP_200_OK)

