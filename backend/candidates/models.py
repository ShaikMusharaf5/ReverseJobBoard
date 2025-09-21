from django.db import models
from users.models import User

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.TextField(blank=True)       # Store comma-separated or free text skills
    projects = models.TextField(blank=True) 
    years_experience = models.PositiveIntegerField()
    education = models.CharField(max_length=128)
    salary_expectation = models.IntegerField()
    availability_status = models.CharField(max_length=32)
    portfolio_link = models.URLField(blank=True)
    avg_rating = models.FloatField(default=0.0)
    profile_views = models.PositiveIntegerField(default=0)

class Skill(models.Model):
    name = models.CharField(max_length=32)

class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
class Resume(models.Model):
    candidate = models.OneToOneField(CandidateProfile, on_delete=models.CASCADE, related_name='resume')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    parsed_skills = models.TextField(blank=True)  # Auto-extracted skills
    parsed_projects = models.TextField(blank=True)  # Auto-extracted projects
