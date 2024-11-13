from django.urls import path
from . import views

app_name = 'application_tracking'

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('add/', views.application_add, name='application_add'),
    path('<int:pk>/', views.application_detail, name='application_detail'),
    path('<int:pk>/edit/', views.application_edit, name='application_edit'),
    path('<int:pk>/delete/', views.application_delete, name='application_delete'),
]
