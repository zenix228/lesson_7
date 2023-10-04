from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from app.models import (
Study_Center,
Teacher,
Student
)
from .serializers import Study_CenterSerializers, TeacherSerializers, StudentSerializers
from .permissions import (Study_CenterDetailPermission,
TeacherPermission,
TeacherDetailPermisison,
StudentPermission,
StudentDetailPermission,
Study_centerPermission
)

@api_view(['GET', 'POST'])
@permission_classes([Study_centerPermission])
def study_center(request):
    if request.method == 'GET':
        study_center = Study_Center.objects.all()
        serializer = Study_CenterSerializers(study_center, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = Study_CenterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST' 'PUT', 'DELETE'])
@permission_classes([Study_CenterDetailPermission])
def study_detail(request, pk):

    study_center = Study_Center.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = Study_CenterSerializers(study_center)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = Study_CenterDetailPermission(Study_Center, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Study_Center.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
@permission_classes([TeacherPermission])
def teacher(request):
    if request.method == 'GET':
        teacher = Teacher.objects.all()
        serializer = TeacherSerializers(teacher)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST' 'PUT', 'DELETE'])
@permission_classes([TeacherDetailPermisison])
def teacher_detail(request, pk):

    teacher = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TeacherSerializers(teacher)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Study_Center.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
@api_view(['POST', 'POST', 'DELETE'])
@permission_classes([StudentPermission])
def student(request):

    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializers(student)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['POST', 'PUT'])
@permission_classes([StudentDetailPermission])
def student_detail(request, pk):

    Teacher = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TeacherSerializers(Teacher)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Student.delete()
        return Response(status=HTTP_204_NO_CONTENT)