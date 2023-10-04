from rest_framework import serializers
from app.models import Study_Center, Teacher, Student

class Study_CenterSerializers(serializers.Serializer):
    class Meta:
        model = Study_Center
        fields = '__all__'

class TeacherSerializers(serializers.Serializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializers(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'