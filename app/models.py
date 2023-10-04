from django.db import models

class Study_Center(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'

class Teacher(models.Model):
    fullname = models.CharField(max_length=250)
    about = models.TextField()
    experience = models.PositiveIntegerField(blank=True, null=True)
    study_center = models.ForeignKey(Study_Center, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.fullname}'
    
class Student(models.Model):
    fullname = models.CharField(max_length=200)
    about = models.TextField()
    phone_number = models.CharField(max_length=100)
    study_center = models.ForeignKey(Study_Center, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)