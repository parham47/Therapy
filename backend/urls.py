from django.urls import path, include, re_path
from django.views.generic import TemplateView
from therapist.views import RedirectSocial

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('api/', include('therapist.urls')),
    path('google/', RedirectSocial.as_view()),
    # path('get_oauth_data/', get_oauth_data.as_view(), name='get_oauth_data')
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
