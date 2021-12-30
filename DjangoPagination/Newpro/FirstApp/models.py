from django.db import models

class Student(models.Model):
    rollno=models.IntegerField()
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=50)
    marks =models.FloatField()
    fees = models.BooleanField(max_length=20)

