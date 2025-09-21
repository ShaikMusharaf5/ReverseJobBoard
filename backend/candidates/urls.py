from django.urls import path
from .views import CandidateProfileView, ResumeUploadView

urlpatterns = [
    path('', CandidateProfileView.as_view()),
    path('upload_resume/', ResumeUploadView.as_view()),
    path('<int:pk>/', CandidateProfileView.as_view(), name='candidate-detail'),

]
