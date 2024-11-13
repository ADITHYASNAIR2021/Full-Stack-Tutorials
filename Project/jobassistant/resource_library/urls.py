from django.urls import path
from . import views

app_name = 'resource_library'

urlpatterns = [
    path('', views.resource_library_view, name='resource_library_view'),
]
