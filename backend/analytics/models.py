from django.db import models

class SearchAnalytics(models.Model):
    role = models.CharField(max_length=128)
    search_count = models.PositiveIntegerField(default=0)
    last_searched = models.DateTimeField(auto_now=True)
