from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .utils import (
    extract_text_from_pdf,
    extract_job_description,
    extract_requirements,
    create_email  
)

def index(request):
    return render(request, 'email_generator/index.html')

def generate_email(request):
    if request.method == 'POST':
        job_link = request.POST.get('job_link')
        resume_file = request.FILES.get('resume_file')

        if not job_link or not resume_file:
            messages.error(request, "Please provide both job link and resume.")
            return redirect('email_generator:index')

        try:
            job_description = extract_job_description(job_link)
            if not job_description:
                messages.error(request, "Failed to extract job description.")
                return redirect('email_generator:index')

            requirements = extract_requirements(job_description)
            if not requirements:
                messages.error(request, "Failed to extract job requirements.")
                return redirect('email_generator:index')

            resume_text = extract_text_from_pdf(resume_file)
            if not resume_text:
                messages.error(request, "Failed to extract text from resume.")
                return redirect('email_generator:index')

            email_text = create_email(job_description, requirements, resume_text)
            if email_text:
                context = {
                    'email_text': email_text
                }
                return render(request, 'email_generator/generated_email.html', context)
            else:
                messages.error(request, "Failed to generate email.")
                return redirect('email_generator:index')

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('email_generator:index')

    return redirect('email_generator:index')
