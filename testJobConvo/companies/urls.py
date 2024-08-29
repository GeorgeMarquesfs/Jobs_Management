from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_job, name='companies_home'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('view_applicants/<int:job_id>/', views.view_applicants, name='view_applicants'),
    path('relatorio/', views.job_report, name='job_report')
]