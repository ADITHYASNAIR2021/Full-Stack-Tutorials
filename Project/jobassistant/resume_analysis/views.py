import re
import fitz  # PyMuPDF
import plotly.express as px
import pandas as pd
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from langchain_groq import ChatGroq
from .models import ResumeAnalysisResult

llm = ChatGroq(
    temperature=0,
    groq_api_key=settings.GROQ_API_KEY,
    model_name="llama-3.1-70b-versatile"
)

def extract_text_from_pdf(pdf_file):

    text = ""
    try:
        # Read the PDF file using PyMuPDF
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def extract_skills(resume_text):

    prompt = f"""
    Extract a comprehensive list of technical and soft skills from the following resume text. Provide the skills as a comma-separated list.

    Resume Text:
    {resume_text}

    Skills:
    """

    try:
        response = llm.invoke(prompt)
        skills = response.content.strip()
        skills_list = [skill.strip() for skill in re.split(',|\n', skills) if skill.strip()]
        return skills_list
    except Exception as e:
        print(f"Error extracting skills: {e}")
        return []

def suggest_keywords(resume_text):

    prompt = f"""
    Analyze the following resume text and suggest additional relevant keywords that can enhance its compatibility with Applicant Tracking Systems (ATS).

    Resume Text:
    {resume_text}

    Suggested Keywords:
    """

    try:
        response = llm.invoke(prompt)
        keywords = response.content.strip()
        keywords_list = [keyword.strip() for keyword in re.split(',|\n', keywords) if keyword.strip()]
        return keywords_list
    except Exception as e:
        print(f"Error suggesting keywords: {e}")
        return []

def create_skill_distribution_chart(skills):

    skill_counts = {}
    for skill in skills:
        skill_counts[skill] = skill_counts.get(skill, 0) + 1
    df = pd.DataFrame(list(skill_counts.items()), columns=['Skill', 'Count'])
    fig = px.bar(df, x='Skill', y='Count', title='Skill Distribution')
    return fig.to_html(full_html=False)

def create_experience_timeline(resume_text):

    prompt = f"""
    From the following resume text, extract the job titles, companies, and durations of employment. Provide the information in a table format with columns: Job Title, Company, Start Year, End Year.

    Resume Text:
    {resume_text}

    Table:
    """

    try:
        response = llm.invoke(prompt)
        table_text = response.content.strip()
        # Parse the table_text to create a DataFrame
        data = []
        lines = table_text.strip().split('\n')
        for line in lines:
            parts = line.split('|')
            if len(parts) == 4:
                job_title = parts[0].strip()
                company = parts[1].strip()
                start_year = int(parts[2].strip())
                end_year = int(parts[3].strip())
                data.append({
                    "Job Title": job_title,
                    "Company": company,
                    "Start Year": start_year,
                    "End Year": end_year
                })
        df = pd.DataFrame(data)
        if not df.empty:
            fig = px.timeline(df, x_start="Start Year", x_end="End Year", y="Job Title", color="Company", title="Experience Timeline")
            fig.update_yaxes(autorange="reversed")
            return fig.to_html(full_html=False)
        else:
            return None
    except Exception as e:
        print(f"Error creating experience timeline: {e}")
        return None

def resume_analysis_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('resume_file')
        if not uploaded_file:
            messages.error(request, "❌ Please upload your resume.")
            return render(request, 'resume_analysis/resume_analysis.html')

        if not uploaded_file.name.endswith('.pdf'):
            messages.error(request, "❌ Please upload a PDF file.")
            return render(request, 'resume_analysis/resume_analysis.html')

        # Extract text from PDF
        resume_text = extract_text_from_pdf(uploaded_file)
        if not resume_text:
            messages.error(request, "❌ Failed to extract text from resume.")
            return render(request, 'resume_analysis/resume_analysis.html')

        # Extract skills
        skills = extract_skills(resume_text)
        # Suggest keywords
        keywords = suggest_keywords(resume_text)
        # Generate skill distribution chart
        skill_chart_html = create_skill_distribution_chart(skills) if skills else None
        # Generate experience timeline chart
        experience_timeline_html = create_experience_timeline(resume_text)

        
        ResumeAnalysisResult.objects.create(
            resume_text=resume_text,
            skills=skills,
            keywords=keywords
        )

        context = {
            'skills': skills,
            'keywords': keywords,
            'skill_chart_html': skill_chart_html,
            'experience_timeline_html': experience_timeline_html,
        }

        return render(request, 'resume_analysis/resume_analysis_result.html', context)
    else:
        return render(request, 'resume_analysis/resume_analysis.html')
