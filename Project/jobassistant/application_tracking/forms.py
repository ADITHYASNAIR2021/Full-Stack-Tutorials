from django import forms
from .models import JobApplication, Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'description']

class JobApplicationForm(forms.ModelForm):
    application_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = JobApplication
        fields = ['company', 'position', 'application_date', 'status', 'notes', 'resume', 'cover_letter']
