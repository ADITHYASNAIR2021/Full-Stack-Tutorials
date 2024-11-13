from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(primary_key=True)
    hobbys = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CourseDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.course
