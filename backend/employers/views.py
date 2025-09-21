from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from .models import EmployerProfile, CandidateRating, Bookmark
from .serializers import (
    EmployerProfileSerializer,
    CandidateRatingSerializer,
    BookmarkSerializer
)
from candidates.models import CandidateProfile

class EmployerProfileView(generics.CreateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
class EmployerProfileDetailView(generics.RetrieveAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return EmployerProfile.objects.get(user=self.request.user)

class RateCandidateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CandidateRatingSerializer(data=request.data)
        if serializer.is_valid():
            rating = serializer.save()
            candidate = rating.candidate
            avg_rating = CandidateRating.objects.filter(candidate=candidate).aggregate(
                avg_rating=Avg('stars')
            )['avg_rating']
            candidate.avg_rating = round(avg_rating or 0.0, 1)
            candidate.save()
            Notification.objects.create(
                user=candidate.user,
                message=f'You received a new rating: {rating.stars} stars',
                url=f'/candidates/{candidate.id}/'
            )
            return Response({
                'message': 'Rating submitted successfully',
                'candidate_avg_rating': candidate.avg_rating
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookmarkListView(generics.ListAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(employer=self.request.user)

class BookmarkDeleteView(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Bookmark.objects.get(
            employer=self.request.user,
            candidate__id=self.kwargs['candidate_id']
        )
