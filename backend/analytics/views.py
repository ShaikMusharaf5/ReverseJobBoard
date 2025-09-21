from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from candidates.models import CandidateProfile
from .models import SearchAnalytics
from django.db.models import Sum

class DashboardView(APIView):
    def get(self, request):
        total_candidates = CandidateProfile.objects.count()
        total_views = CandidateProfile.objects.aggregate(total=Sum('profile_views'))['total'] or 0
        top_searches = list(SearchAnalytics.objects.order_by('-search_count')[:5].values('role', 'search_count'))
        return Response({
            'total_candidates': total_candidates,
            'total_profile_views': total_views,
            'top_searches': top_searches,
        })


# Create your views here.
