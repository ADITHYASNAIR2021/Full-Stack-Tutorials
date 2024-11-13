from django.contrib import admin
from .models import LearningPath

@admin.register(LearningPath)
class LearningPathAdmin(admin.ModelAdmin):
    list_display = ('goal', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('goal', 'user__username')
