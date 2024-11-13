# application_tracking/admin.py

from django.contrib import admin
from .models import Company, JobApplication

admin.site.register(Company)
admin.site.register(JobApplication)
