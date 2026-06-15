from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)   # roll number
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)   # contact number

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
