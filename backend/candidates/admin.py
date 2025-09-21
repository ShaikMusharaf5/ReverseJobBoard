from django.contrib import admin
from .models import CandidateProfile, Resume

@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'years_experience', 'avg_rating')
    search_fields = ('user__username', 'skills', 'projects')
    list_filter = ('availability_status',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate', 'uploaded_at')
    search_fields = ('candidate__user__username',)
    readonly_fields = ('parsed_skills', 'parsed_projects')
