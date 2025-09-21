from django.db import models
from users.models import User
from candidates.models import CandidateProfile
from django.contrib.auth import get_user_model
from candidates.models import CandidateProfile


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=128)
    website = models.URLField(blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CandidateRating(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_ratings')
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='received_ratings')
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
User = get_user_model()

class Bookmark(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='bookmarked_by')
    created_at = models.DateTimeField(auto_now_add=True)   
    class Meta:
        unique_together = ('employer', 'candidate')  # One rating per employer-candidate pair
