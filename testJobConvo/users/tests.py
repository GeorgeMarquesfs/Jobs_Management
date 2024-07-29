from django.test import TestCase
from django.urls import reverse
from users.models import JobPosting, Application

class ViewApplicantsTest(TestCase):

    def setUp(self):
        
        self.job = JobPosting.objects.create(
            title='Desenvolvedor Python',
            salary_range='2000_to_3000',
            education_level='superior'
        )
        self.application1 = Application.objects.create(
            job=self.job,
            name='Candidato 1',
            salary_expectation=2500,
            experience='2 anos de experiência',
            highest_education='superior'
        )
        self.application2 = Application.objects.create(
            job=self.job,
            name='Candidato 2',
            salary_expectation=1500,
            experience='3 anos de experiência',
            highest_education='tecnologo'
        )

    def test_view_applicants(self):
        url = reverse('view_applicants', args=[self.job.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Desenvolvedor Python')
        self.assertContains(response, 'Candidato 1')
        self.assertContains(response, 'Candidato 2')
