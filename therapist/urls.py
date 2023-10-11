from django.urls import path
from .views import (
   
    AppointmentListCreateView, AppointmentRetrieveUpdateDestroyView,
    MoodEntryListCreateView, MoodEntryRetrieveUpdateDestroyView,
    ThoughtProcessingListCreateView, ThoughtProcessingRetrieveUpdateDestroyView,PsychologicalDisorderListCreateView, PsychologicalDisorderRetrieveUpdateDestroyView,
    RedirectSocial,UserList,AppointmentShow
)


urlpatterns = [
    path('list-patients/', UserList.as_view(), name='patients-list'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-create'),
    path('appointment/', AppointmentShow.as_view(), name='appointment-show'),

    path('appointments/<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail'),
    path('mood-entries/', MoodEntryListCreateView.as_view(), name='mood-entry-list'),
    path('mood-entries/<int:pk>/', MoodEntryRetrieveUpdateDestroyView.as_view(), name='mood-entry-detail'),
    path('thought-processings/', ThoughtProcessingListCreateView.as_view(), name='thought-processing-list'),
    path('thought-processings/<int:pk>/', ThoughtProcessingRetrieveUpdateDestroyView.as_view(), name='thought-processing-detail'),
    path('thought-processings/', PsychologicalDisorderListCreateView.as_view(), name='thought-processing-list'),
    path('thought-processings/<int:pk>/', PsychologicalDisorderRetrieveUpdateDestroyView.as_view(), name='thought-processing-detail'),
    # path('google/', RedirectSocial.as_view(),),
    
 ]