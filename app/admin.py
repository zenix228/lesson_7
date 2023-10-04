from django.contrib import admin
from .models import Study_Center, Teacher, Student

@admin.register(Study_Center)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'about')
    list_display_links = ('id', 'fullname', 'about')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'about', 'teacher')
    list_display_links = ('id', 'fullname', 'about', 'teacher')