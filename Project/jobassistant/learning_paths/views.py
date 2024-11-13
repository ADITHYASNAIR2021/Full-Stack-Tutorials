import json
import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from langchain_groq import ChatGroq
from django.conf import settings
from .models import LearningPath

llm = ChatGroq(
    temperature=0.7,
    groq_api_key=settings.GROQ_API_KEY,
    model_name="llama-3.1-70b-versatile"
)

@login_required
def generate_learning_path(request):
    if request.method == 'POST':
        goal = request.POST.get('goal', '').strip()
        if goal:
            try:
                prompt = f"""
                You are an educational consultant. Create a personalized learning path for someone aiming to become a {goal}.
                Include a list of topics with titles, descriptions, and relevant YouTube video URLs.
                Output the results in valid JSON format without any extra text or explanations.

                Format:
                [
                    {{
                        "title": "Topic Title",
                        "description": "Brief description.",
                        "video_url": "YouTube Video URL"
                    }},
                    ...
                ]
                Ensure that the JSON is properly formatted and only include the JSON in your response.
                """

                response = llm.invoke(prompt)
                content = response.content.strip()
                print(f"LLM Response Content: {content}")  # Debug statement

                # Extract JSON from the response
                json_content = extract_json(content)
                print(f"Extracted JSON Content: {json_content}")  # Debug statement

                learning_path = json.loads(json_content)

                # Save to database
                LearningPath.objects.create(user=request.user, goal=goal, content=learning_path)

                return render(request, 'learning_paths/learning_path.html', {
                    'goal': goal,
                    'learning_path': learning_path
                })
            except ValueError as ve:
                messages.error(request, 'Failed to parse the generated learning path. Please try again.')
                print(f"JSON Parsing Error: {ve}")
            except Exception as e:
                messages.error(request, 'An error occurred while generating your learning path.')
                print(f"Error: {e}")
        else:
            messages.error(request, 'Please enter your career goal.')
    return render(request, 'learning_paths/generate_learning_path.html')

def extract_json(text):

    json_pattern = r'\[.*\]'
    match = re.search(json_pattern, text, re.DOTALL)
    if match:
        return match.group(0)
    else:
        raise ValueError("No JSON content found in the response.")
