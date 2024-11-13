from django.urls import path
from . import views

app_name = 'resume_analysis'

urlpatterns = [
    path('', views.resume_analysis_view, name='resume_analysis_view'),
]
