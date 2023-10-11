from django.urls import path
from .views import GoogleOauthAPIView

urlpatterns = [
    path('', GoogleOauthAPIView.as_view(), name='google_oauth'),
]