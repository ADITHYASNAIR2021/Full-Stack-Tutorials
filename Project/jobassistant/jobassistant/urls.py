# jobassistant/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('email-generator/', include('email_generator.urls')),
    path('cover-letter-generator/', include('cover_letter_generator.urls')),
    path('resume-analysis/', include('resume_analysis.urls')),
    path('application-tracking/', include('application_tracking.urls')),
    path('interview-preparation/', include('interview_preparation.urls')),
    path('learning-paths/', include('learning_paths.urls')),
    path('networking-opportunities/', include('networking_opportunities.urls')),
    path('resource-library/', include('resource_library.urls')),
    path('chatbot-support/', include('chatbot_support.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
