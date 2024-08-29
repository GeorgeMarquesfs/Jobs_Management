from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'salary_expectation', 'experience', 'highest_education']
        labels = {
            'name': 'Nome',
            'salary_expectation': 'Pretensão Salarial',
            'experience': 'Experiência',
            'highest_education': 'Última Escolaridade'
        }
    
    job_title = forms.CharField(widget=forms.HiddenInput())