from django.shortcuts import render
from rest_framework import status,permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CandidateProfile
from .serializers import CandidateProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CandidateProfile
from .serializers import CandidateProfileSerializer

class CandidateDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        try:
            candidate = CandidateProfile.objects.get(pk=pk)
            candidate.profile_views += 1
            candidate.save()
            serializer = CandidateProfileSerializer(candidate)
            return Response(serializer.data)
        except CandidateProfile.DoesNotExist:
            return Response({"detail": "Candidate not found."}, status=status.HTTP_404_NOT_FOUND)


class CandidateProfileView(generics.CreateAPIView):
    serializer_class = CandidateProfileSerializer
    queryset = CandidateProfile.objects.all()
class ResumeUploadView(APIView):
    def post(self, request):
        candidate_id = request.data.get('candidate_id')
        resume_file = request.FILES.get('resume')
        
        if not candidate_id or not resume_file:
            return Response({
                'error': 'candidate_id and resume file are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Save file and extract skills/projects using NLP
            extracted_skills = ["Python", "Django"]  # Replace with actual NLP parsing
            extracted_projects = ["Portfolio", "Job Board"]
            
            return Response({
                'message': 'Resume uploaded successfully',
                'extracted_skills': extracted_skills,
                'extracted_projects': extracted_projects,
                'filename': resume_file.name
            })
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UpdateCandidateFromResumeView(APIView):
    def post(self, request):
        candidate_id = request.data.get('candidate_id')
        resume_file = request.FILES.get('resume')
        
        try:
            candidate = CandidateProfile.objects.get(id=candidate_id)
            
            # Parse resume and extract data
            parsed_skills = "Python, Django, Machine Learning"  # From NLP
            parsed_projects = "Job Portal, E-commerce Website"  # From NLP
            
            # Update candidate profile with parsed data
            candidate.skills = parsed_skills
            candidate.projects = parsed_projects
            candidate.save()
            
            return Response({
                'message': 'Profile updated with resume data',
                'updated_skills': parsed_skills,
                'updated_projects': parsed_projects
            })
        except CandidateProfile.DoesNotExist:
            return Response({'error': 'Candidate not found'}, status=404)
