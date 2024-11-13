from django.urls import path
from . import views

app_name = 'chatbot_support'

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('get-response/', views.get_response, name='get_response'),
]
