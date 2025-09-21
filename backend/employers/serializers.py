from rest_framework import serializers
from .models import EmployerProfile, CandidateRating,Bookmark

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = '__all__'

class CandidateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateRating
        fields = '__all__'
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'employer', 'candidate', 'created_at']
        read_only_fields = ['created_at']