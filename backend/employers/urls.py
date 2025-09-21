from django.urls import path
from .views import EmployerProfileView,EmployerProfileDetailView, RateCandidateView,BookmarkCreateView, BookmarkListView, BookmarkDeleteView

urlpatterns = [
    path('profile/', EmployerProfileView.as_view(), name='employer-profile'),
    path('rate-candidate/', RateCandidateView.as_view(), name='rate-candidate'),
    path('bookmarks/', BookmarkListView.as_view(), name='bookmark-list'),
    path('profile/view/', EmployerProfileDetailView.as_view(), name='employer-profile-detail'),

    path('bookmarks/add/', BookmarkCreateView.as_view(), name='bookmark-add'),
    path('bookmarks/remove/<int:candidate_id>/', BookmarkDeleteView.as_view(), name='bookmark-remove'),
]
