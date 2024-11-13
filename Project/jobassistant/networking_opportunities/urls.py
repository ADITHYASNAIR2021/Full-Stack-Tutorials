from django.urls import path
from . import views

app_name = 'networking_opportunities'

urlpatterns = [
    path('', views.networking_opportunities_view, name='networking_opportunities_view'),
]
