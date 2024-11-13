from django.urls import path
from . import views

app_name = 'email_generator'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate_email, name='generate_email'),
]
