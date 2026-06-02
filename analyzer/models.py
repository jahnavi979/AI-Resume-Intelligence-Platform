from django.db import models
from django.contrib.auth.models import User

class ResumeUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.file.name}"

class AnalysisResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(ResumeUpload, on_delete=models.CASCADE)
    job_description = models.TextField()
    ats_score = models.FloatField()
    matched_keywords = models.TextField(blank=True)
    missing_keywords = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis {self.id} - {self.user.username}"