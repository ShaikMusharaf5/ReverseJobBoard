from django.urls import path
from .views import RegisterView, LoginView, CandidateSearchView

app_name = 'core'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', CandidateSearchView.as_view(), name='search'),
]
