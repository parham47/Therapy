from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.views import APIView

from rest_framework import status

class GoogleOauthAPIView(APIView):
    def get(self, request):
        # Extracting the 'code' and 'state' parameters from the GET request
        code = request.GET.get('code', None)
        state = request.GET.get('state', None)
        print(code)  # Fixed: Use 'code' variable instead of the string "code"

        if not code or not state:
            # If 'code' or 'state' parameters are missing, return an error response
            return Response({"error": "Missing 'code' or 'state' parameters"}, status=status.HTTP_400_BAD_REQUEST)

        # Fixed: Use 'authorization_code' as a string, not an undefined variable
        details = {
            'state': state,
            'code': code,
            'client_id': '855150297727-frj54btbp93i1g50tglt5klg7g1jvug6.apps.googleusercontent.com',
            'client_secret': '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',
            'redirect_uri': 'https://7bfb-31-56-195-93.ngrok-free.app/auth/o/google-oauth2/',
            'grant_type': 'authorization_code',  # Fixed: Add quotes to 'authorization_code'
        }

        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        # Making the POST request to the specified URL
        API_URL = 'https://oauth2.googleapis.com/token/'  # Fixed: Replace 'YOUR_API_URL' with the actual URL
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

