from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_home, name='users_home'), 
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),  
]