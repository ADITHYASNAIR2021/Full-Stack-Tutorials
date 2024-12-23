from django.shortcuts import render
from .models import Resource
from django.core.paginator import Paginator


def resource_library_view(request):
    query = request.GET.get('q')
    if query:
        resources_list = Resource.objects.filter(title__icontains=query)
    else:
        resources_list = Resource.objects.all()
    paginator = Paginator(resources_list, 10) 

    page_number = request.GET.get('page')
    resources = paginator.get_page(page_number)
    return render(request, 'resource_library/resource_library.html', {'resources': resources})