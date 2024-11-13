from django.urls import path
from . import views

app_name = 'learning_paths'

urlpatterns = [
    path('', views.generate_learning_path, name='generate_learning_path'),
]
