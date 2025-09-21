from django.contrib import admin
from .models import EmployerProfile, CandidateRating

@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_name', 'created_at')
    search_fields = ('user__username', 'company_name')

@admin.register(CandidateRating)
class CandidateRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'employer', 'candidate', 'stars', 'created_at')
    list_filter = ('stars',)
    search_fields = ('employer__username', 'candidate__user__username')
