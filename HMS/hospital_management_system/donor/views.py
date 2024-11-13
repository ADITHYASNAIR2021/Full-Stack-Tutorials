from django.shortcuts import render, redirect
from .models import Student, CourseDetails
from .forms import StudentForm, CourseDetailsForm

def donor(request):
    students = Student.objects.all()
    courses = CourseDetails.objects.all()

    if request.method == 'POST':
        if 'student_form' in request.POST:
            student_form = StudentForm(request.POST)
            if student_form.is_valid():
                student_form.save()
                return redirect('donor')  
            
        elif 'course_form' in request.POST:
            course_form = CourseDetailsForm(request.POST)
            if course_form.is_valid():
                course_form.save()
                return redirect('donor')  
    else:
        student_form = StudentForm()
        course_form = CourseDetailsForm()

    return render(request, 'donor.html', {'students': students, 'courses': courses, 'student_form': student_form, 'course_form': course_form })
