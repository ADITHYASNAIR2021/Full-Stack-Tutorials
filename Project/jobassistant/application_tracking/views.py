from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobApplication, Company
from .forms import JobApplicationForm, CompanyForm
from django.contrib import messages

@login_required
def application_list(request):
    applications = JobApplication.objects.filter(user=request.user).order_by('-application_date')
    return render(request, 'application_tracking/application_list.html', {'applications': applications})


@login_required
def application_add(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        company_form = CompanyForm(request.POST)
        if form.is_valid() and company_form.is_valid():
            company_name = company_form.cleaned_data['name']
            company, created = Company.objects.get_or_create(name=company_name, defaults={
                'website': company_form.cleaned_data.get('website'),
                'description': company_form.cleaned_data.get('description'),
            })

            application = form.save(commit=False)
            application.user = request.user
            application.company = company
            application.save()
            messages.success(request, 'Application added successfully.')
            return redirect('application_tracking:application_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = JobApplicationForm()
        company_form = CompanyForm()
    return render(request, 'application_tracking/application_form.html', {
        'form': form,
        'company_form': company_form
    })

@login_required
def application_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    return render(request, 'application_tracking/application_detail.html', {'application': application})

@login_required
def application_edit(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application updated successfully.')
            return redirect('application_tracking:application_detail', pk=pk)
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'application_tracking/application_form.html', {'form': form})

@login_required
def application_delete(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Application deleted successfully.')
        return redirect('application_tracking:application_list')
    return render(request, 'application_tracking/application_confirm_delete.html', {'application': application})
