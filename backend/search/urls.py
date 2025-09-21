from django.urls import path
from .views import CandidateSearchView

urlpatterns = [
    path('', CandidateSearchView.as_view(), name='candidate-search'),
]
