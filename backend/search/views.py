from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from candidates.models import CandidateProfile

class CandidateSearchView(APIView):
    def get(self, request):
        role = request.GET.get('role', '').lower()
        min_exp = int(request.GET.get('min_experience', 0))
        min_rating = float(request.GET.get('min_rating', 0.0))

        # Define required skills/projects per role
        ROLE_REQUIREMENTS = {
            'python developer': {
                'skills': ['python', 'django', 'rest api'],
                'projects': ['web', 'api']
            },
            'data scientist': {
                'skills': ['python', 'machine learning', 'pandas'],
                'projects': ['analysis', 'model']
            },
            # Add more roles...
        }
        req = ROLE_REQUIREMENTS.get(role, {'skills': [], 'projects': []})

        results = []
        for c in CandidateProfile.objects.all():
            ticks = 0
            skills = [s.strip().lower() for s in c.skills.split(',') if s]
            projects = [p.strip().lower() for p in c.projects.split(',') if p]

            # Skill ticks
            for skill in req['skills']:
                if skill in skills:
                    ticks += 1

            # Project ticks
            for proj in req['projects']:
                if proj in projects:
                    ticks += 1

            # Experience tick
            if c.years_experience >= min_exp:
                ticks += 1

            # Rating tick
            if c.avg_rating >= min_rating:
                ticks += 1

            results.append({
                'id': c.id,
                'bio': c.bio,
                'skills': skills,
                'projects': projects,
                'years_experience': c.years_experience,
                'avg_rating': c.avg_rating,
                'tick_count': ticks
            })

        # Sort by tick_count descending, then rating, then experience
        results.sort(key=lambda x: (x['tick_count'], x['avg_rating'], x['years_experience']), reverse=True)

        return Response(results)


# Create your views here.
