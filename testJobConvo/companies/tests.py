from django.test import TestCase
from users.models import JobPosting, Application

class ApplicationModelTest(TestCase):

    def setUp(self):
        # Cria uma vaga e uma aplicação
        self.job = JobPosting.objects.create(
            title='Desenvolvedor Python',
            salary_range='2000_to_3000',
            education_level='superior'
        )
        self.application = Application.objects.create(
            job=self.job,
            name='Candidato 1',
            salary_expectation=2500,
            experience='2 anos de experiência',
            highest_education='superior'
        )

