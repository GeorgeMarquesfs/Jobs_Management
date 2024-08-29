from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class JobPosting(models.Model):
    SALARY_CHOICES = [
        ('up_to_1000', 'Até 1.000'),
        ('1000_to_2000', 'De 1.000 a 2.000'),
        ('2000_to_3000', 'De 2.000 a 3.000'),
        ('above_3000', 'Acima de 3.000'),
    ]

    EDUCATION_CHOICES = [
        ('fundamental', 'Ensino fundamental'),
        ('medio', 'Ensino médio'),
        ('tecnologo', 'Tecnólogo'),
        ('superior', 'Ensino Superior'),
        ('pos_mba_mestrado', 'Pós / MBA / Mestrado'),
        ('doutorado', 'Doutorado'),
    ]

    title = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=50, choices=SALARY_CHOICES)
    education_level = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Application(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='company_applications')
    job_title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.TextField()
    highest_education = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.name} - {self.job_title}"
    
    def calculate_score(self):
        score = 0

        salary_ranges = {
            'up_to_1000': (0, 1000),
            '1000_to_2000': (1000, 2000),
            '2000_to_3000': (2000, 3000),
            'above_3000': (3000, float('inf')),
        }

        job_salary_range = dict(salary_ranges).get(self.job.salary_range)
        if job_salary_range and job_salary_range[0] <= self.salary_expectation <= job_salary_range[1]:
            score += 1

        education_order = {
            'fundamental': 1,
            'medio': 2,
            'tecnologo': 3,
            'superior': 4,
            'pos_mba_mestrado': 5,
            'doutorado': 6,
        }

        job_education_level = self.job.education_level
        candidate_education_level = self.highest_education

        if education_order.get(candidate_education_level, 0) >= education_order.get(job_education_level, 0):
            score += 1

        return score
    



