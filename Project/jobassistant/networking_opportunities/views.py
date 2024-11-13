import re
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key=settings.GROQ_API_KEY,
    model_name="llama-3.1-70b-versatile"
)

def networking_opportunities_view(request):
    if request.method == 'POST':
        user_skills = request.POST.get('user_skills', '').strip()
        industry = request.POST.get('industry', '').strip()
        if not user_skills or not industry:
            messages.error(request, '❌ Please enter both key skills and industry.')
            return render(request, 'networking_opportunities/networking_form.html')
        prompt = f"""
        Based on the following skills: {user_skills}, and industry: {industry}, suggest relevant LinkedIn groups, professional organizations, and industry events for networking.

        Provide the suggestions in a numbered list format, including brief descriptions and links if available.
        """
        try:
            # Invoke the LLM
            response = llm.invoke(prompt)
            suggestions = response.content.strip()
            # Process the suggestions into a list
            suggestions_list = re.split(r'\n\d+\.', suggestions)
            suggestions_list = [s.strip() for s in suggestions_list if s.strip()]
            return render(request, 'networking_opportunities/networking_results.html', {
                'suggestions': suggestions_list,
                'user_skills': user_skills,
                'industry': industry
            })
        except Exception as e:
            messages.error(request, f"❌ Error fetching networking opportunities: {e}")
            return render(request, 'networking_opportunities/networking_form.html')
    else:
        return render(request, 'networking_opportunities/networking_form.html')
