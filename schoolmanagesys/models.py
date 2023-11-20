from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_choices = (
        (1, "Mathematics"),
        (2, "Physics"),
        (3, "Chemistry"),
        (4, "Biology"),
    )
    
    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    courses = models.ManyToManyField(Course, related_name='students')
    
    can_see_grades = models.BooleanField(default=True)
    can_see_attendance = models.BooleanField(default=True)
    assigned_classes = models.ManyToManyField(Course, related_name='teachers')
    course_choice = models.IntegerField(choices=Course.course_choices, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Teacher(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    can_assign_classes = models.BooleanField(default=True)
    can_assign_courses = models.BooleanField(default=True)
    can_edit_student_attendance = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

