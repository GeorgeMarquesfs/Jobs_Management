from django.db import models
from companies.models import JobPosting
from django.utils import timezone

class Application(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='user_applications')
    job_title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.TextField()
    highest_education = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.job_title}"