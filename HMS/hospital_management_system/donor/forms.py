from django import forms
from .models import Student, CourseDetails

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'hobbys']

class CourseDetailsForm(forms.ModelForm):
    class Meta:
        model = CourseDetails
        fields = ['student', 'course'] 
