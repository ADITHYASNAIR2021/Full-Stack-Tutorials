from django.urls import path
from . import views

app_name = 'interview_preparation'

urlpatterns = [
    path('', views.interview_preparation_view, name='interview_preparation'),
]
