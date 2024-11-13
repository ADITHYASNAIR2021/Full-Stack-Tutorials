from django.db import models

class ResumeAnalysisResult(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    resume_text = models.TextField()
    skills = models.JSONField()
    keywords = models.JSONField()

    def __str__(self):
        return f"Resume Analysis - {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
