from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=50)
    fees = models.IntegerField()
    marks = models.IntegerField()

    def __str__(self):
        return self.student_name


class School(models.Model):
    school_name = models.CharField(max_length=100)
    joining_date = models.DateField(auto_now=True, blank=True)
    pointer = models.DecimalField(max_digits=10, decimal_places=2)
    email_id = models.EmailField(max_length=250)
    student_pic = models.ImageField(upload_to=None, height_field=None,
                                    width_field=None, max_length=100, blank=True)
    school_students = models.IntegerField()
    student_details = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.school_name
