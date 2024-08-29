# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_home, name='users_home'),  # Página inicial dos usuários
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),  # Página de aplicação para vaga
]