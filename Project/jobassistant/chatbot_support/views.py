from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from langchain_groq import ChatGroq
import json

llm = ChatGroq(
    temperature=0.7,
    groq_api_key=settings.GROQ_API_KEY,
    model_name="llama-3.1-70b-versatile"
)

def chatbot(request):
    return render(request, 'chatbot_support/chatbot.html')

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        if user_message:
            try:
                # Generate a response using Groq API
                prompt = f"User: {user_message}\nAssistant:"
                response = llm.invoke(prompt)
                bot_response = response.content.strip()

                return JsonResponse({'message': bot_response})
            except Exception as e:
                return JsonResponse({'message': 'Sorry, an error occurred while processing your request.'}, status=500)
        else:
            return JsonResponse({'message': 'No message received.'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)
