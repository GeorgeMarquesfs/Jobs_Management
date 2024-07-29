from django.shortcuts import render, redirect, get_object_or_404
from companies.models import JobPosting
from companies.models import Application as CompaniesApplication
from users.models import Application
from django.db.models import Count, F
from django.utils import timezone 
from django.db.models.functions import ExtractMonth
import calendar


def create_job(request):
    if request.method == 'POST':
        job_title = request.POST['job_title']
        salary_range = request.POST['salary_range']
        education_level = request.POST['education_level']

        JobPosting.objects.create(
            title=job_title,
            salary_range=salary_range,
            education_level=education_level
        )

        return redirect('companies_home')

    job_postings = JobPosting.objects.all()
    return render(request, 'companies/home.html', {'job_postings': job_postings})

def edit_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    if request.method == 'POST':
        job.title = request.POST['job_title']
        job.salary_range = request.POST['salary_range']
        job.education_level = request.POST['education_level']
        job.save()
        return redirect('companies_home')
    
    return render(request, 'companies/edit_job.html', {'job': job})

def delete_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    job.delete()
    return redirect('companies_home')

def job_applications(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    applications = job.applications.all()
    return render(request, 'companies/job_applications.html', {'job': job, 'applications': applications})


def view_applicants(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    applicants = job.user_applications.all()

    for applicant in applicants:
        applicant.score = CompaniesApplication.calculate_score(applicant)
      
    context = {
        'job': job,
        'applicants': applicants,
    }

    return render(request, 'companies/view_applicants.html', context)


def job_report(request):
    current_year = timezone.now().year

    jobs_by_month = (
        JobPosting.objects.annotate(month=ExtractMonth('created_at'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    job_months = [calendar.month_name[job['month']] for job in jobs_by_month]
    job_counts = [job['count'] for job in jobs_by_month]

    
    applications_by_month = (
        Application.objects.annotate(month=ExtractMonth('created_at'))
        .values('month', 'job__title')
        .annotate(count=Count('id'))
        .order_by('month', 'job__title')
    )


    all_months = [calendar.month_name[i] for i in range(1, 13)]
    application_months_set = {calendar.month_name[app['month']] for app in applications_by_month}
    application_months = [month for month in all_months if month in application_months_set]

    job_titles = sorted(list({app['job__title'] for app in applications_by_month}))


    application_counts = [[0 for _ in job_titles] for _ in application_months]


    for app in applications_by_month:
        month_index = application_months.index(calendar.month_name[app['month']])
        job_index = job_titles.index(app['job__title'])
        application_counts[month_index][job_index] = app['count']

    context = {
        'job_months': job_months,
        'job_counts': job_counts,
        'application_months': application_months,
        'job_titles': job_titles,
        'application_counts': application_counts,
    }

    return render(request, 'companies/job_report.html', context)
