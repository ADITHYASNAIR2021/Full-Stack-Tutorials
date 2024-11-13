from django.shortcuts import render
from .models import Resource

def resource_library_view(request):
    resources = Resource.objects.all()
    return render(request, 'resource_library/resource_library.html', {'resources': resources})

def resource_library_view(request):
    query = request.GET.get('q')
    if query:
        resources = Resource.objects.filter(title__icontains=query)
    else:
        resources = Resource.objects.all()
    return render(request, 'resource_library/resource_library.html', {'resources': resources})

from django.core.paginator import Paginator

def resource_library_view(request):
    query = request.GET.get('q')
    if query:
        resources_list = Resource.objects.filter(title__icontains=query)
    else:
        resources_list = Resource.objects.all()
    paginator = Paginator(resources_list, 10)  # Show 10 resources per page

    page_number = request.GET.get('page')
    resources = paginator.get_page(page_number)
    return render(request, 'resource_library/resource_library.html', {'resources': resources})