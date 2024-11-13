from django.urls import path
from . import views

app_name = 'cover_letter_generator'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate_cover_letter_view, name='generate_cover_letter'),
]
