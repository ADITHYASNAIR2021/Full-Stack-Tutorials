from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key=settings.GROQ_API_KEY,
    model_name="llama-3.1-70b-versatile",
    max_tokens=4000,
)

def generate_interview_questions(job_title, company_name):
    prompt = f"""
    As an expert interviewer, generate a list of 50 medium to hard-level interview questions for a {job_title} position at {company_name}. Provide detailed and comprehensive answers to each question.

    Format your response exactly as follows:

    Question 1: [Question text]
    Answer 1: [Answer text]

    Question 2: [Question text]
    Answer 2: [Answer text]

    ...

    Continue this pattern up to Question 50.

    Do not include any additional text or explanations outside of this format.
    """
    try:
        response = llm.invoke(prompt)
        if response and hasattr(response, 'content'):
            raw_output = response.content.strip()
            interview_questions = parse_questions_and_answers(raw_output)
            return interview_questions
        else:
            print("LLM returned an empty or invalid response.")
            return None
    except Exception as e:
        print(f"Error generating interview questions: {e}")
        return None

def parse_questions_and_answers(raw_output):
    import re
    pattern = r"Question \d+: (.*?)\nAnswer \d+: (.*?)(?=Question \d+:|$)"
    matches = re.findall(pattern, raw_output, re.DOTALL)
    interview_questions = []
    for question, answer in matches:
        interview_questions.append({
            'question': question.strip(),
            'answer': answer.strip()
        })
    return interview_questions

def interview_preparation_view(request):
    if request.method == 'POST':
        try:
            job_title = request.POST.get('job_title')
            company_name = request.POST.get('company_name')

            print(f"Received job_title: {job_title}")
            print(f"Received company_name: {company_name}")

            if not job_title or not company_name:
                messages.error(request, "❌ Please provide both job title and company name.")
                return render(request, 'interview_preparation/interview_preparation.html')

            interview_questions = generate_interview_questions(job_title, company_name)
            if not interview_questions:
                messages.error(request, "❌ Failed to generate interview questions. Please try again later.")
                return render(request, 'interview_preparation/interview_preparation.html')

            topic = f"{job_title} at {company_name}"

            context = {
                'topic': topic,
                'interview_questions': interview_questions,
            }
            return render(request, 'interview_preparation/interview_questions.html', context)
        except Exception as e:
            print(f"Exception in interview_preparation_view: {e}")
            messages.error(request, "❌ An unexpected error occurred. Please try again later.")
            return render(request, 'interview_preparation/interview_preparation.html')
    else:
        return render(request, 'interview_preparation/interview_preparation.html')
