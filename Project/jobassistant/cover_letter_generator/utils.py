import fitz  
import requests
from bs4 import BeautifulSoup
from django.conf import settings
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key=settings.GROQ_API_KEY,
    model_name="llama-3.1-70b-versatile"
)

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {e}")

def extract_job_description(job_link):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(job_link, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        job_description = soup.get_text(separator='\n')
        return job_description.strip()
    except Exception as e:
        raise Exception(f"Error fetching job description: {e}")

def extract_requirements(job_description):
    prompt = f"""
    The following is a job description:

    {job_description}

    Extract the list of job requirements, qualifications, and skills from the job description. Provide them as a numbered list.

    Requirements:
    """
    try:
        response = llm.invoke(prompt)
        requirements = response.content.strip()
        return requirements
    except Exception as e:
        raise Exception(f"Error extracting requirements: {e}")

def create_cover_letter(job_description, requirements, resume_text):
    prompt = f"""
    You are Adithya S Nair, a recent Computer Science graduate specializing in Artificial Intelligence and Machine Learning. Craft a personalized cover letter to a potential employer based on the following information:

    **Job Description:**
    {job_description}

    **Extracted Requirements:**
    {requirements}

    **Your Resume:**
    {resume_text}

    **Cover Letter Requirements:**
    - **Introduction:** Introduce yourself and express interest in the specific position.
    - **Alignment:** Highlight how your skills and experiences match the job requirements.
    - **Company Fit:** Discuss why you are interested in the company and how you can contribute.
    - **Closing:** Thank the employer for their consideration and express eagerness to discuss further.

    The cover letter should be professional, concise, and tailored to the job description.
    """
    try:
        response = llm.invoke(prompt)
        cover_letter_text = response.content.strip()
        return cover_letter_text
    except Exception as e:
        raise Exception(f"Error generating cover letter: {e}")
