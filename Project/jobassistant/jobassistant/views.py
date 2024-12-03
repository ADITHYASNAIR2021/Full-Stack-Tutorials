from django.contrib.auth import logout
from django.shortcuts import render, redirect

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home:landing_page')  
    else:
        return render(request, 'registration/logout.html')
