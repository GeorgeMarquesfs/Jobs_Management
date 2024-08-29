from django.shortcuts import render, get_object_or_404, redirect
from companies.models import JobPosting
from .models import Application
from .forms import ApplicationForm

def users_home(request):
    job_postings = JobPosting.objects.all()
    return render(request, 'users/home.html', {'job_postings': job_postings})

def apply_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.job_title = job.title
            application.save()
            print(f"Application saved: {application.name} for job {application.job_title}")
            return redirect('users_home')
        else:
            print("Form is not valid")
    else:
        form = ApplicationForm(initial={'job_title': job.title})
    return render(request, 'users/apply.html', {'job': job, 'form': form})