from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import (
    extract_text_from_pdf,
    extract_job_description,
    extract_requirements,
    create_cover_letter
)

def index(request):
    return render(request, 'cover_letter_generator/index.html')

def generate_cover_letter_view(request):
    if request.method == 'POST':
        job_link = request.POST.get('job_link')
        resume_file = request.FILES.get('resume_file')

        if not job_link or not resume_file:
            messages.error(request, "Please provide both job link and resume.")
            return redirect('cover_letter_generator:index')

        try:
            job_description = extract_job_description(job_link)
            if not job_description:
                messages.error(request, "Failed to extract job description.")
                return redirect('cover_letter_generator:index')

            requirements = extract_requirements(job_description)
            if not requirements:
                messages.error(request, "Failed to extract job requirements.")
                return redirect('cover_letter_generator:index')

            resume_text = extract_text_from_pdf(resume_file)
            if not resume_text:
                messages.error(request, "Failed to extract text from resume.")
                return redirect('cover_letter_generator:index')

            cover_letter_text = create_cover_letter(job_description, requirements, resume_text)
            if cover_letter_text:
                context = {
                    'cover_letter_text': cover_letter_text
                }
                return render(request, 'cover_letter_generator/generated_cover_letter.html', context)
            else:
                messages.error(request, "Failed to generate cover letter.")
                return redirect('cover_letter_generator:index')

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('cover_letter_generator:index')

    return redirect('cover_letter_generator:index')
