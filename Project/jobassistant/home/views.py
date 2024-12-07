from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail  
from django.conf import settings
from django.contrib.auth import logout

def landing_page(request):
    return render(request, 'home/index.html') 


def landing_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_type = request.POST.get('feedback_type')
        feedback_content = request.POST.get('feedback')

        send_mail(
            subject=f'Feedback from {name}: {feedback_type}',
            message=feedback_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['your_email@example.com'],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for your feedback!')
        return redirect('home:landing_page')
    return render(request, 'base.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home:landing_page') 
    else:
        return render(request, 'registration/logout.html')
