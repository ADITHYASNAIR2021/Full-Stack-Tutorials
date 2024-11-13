from django.contrib import admin
from .models import ResumeAnalysisResult

@admin.register(ResumeAnalysisResult)
class ResumeAnalysisResultAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at',)
    readonly_fields = ('uploaded_at', 'resume_text', 'skills', 'keywords')
    search_fields = ('resume_text',)
