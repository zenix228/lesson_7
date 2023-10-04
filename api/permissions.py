from rest_framework.permissions import BasePermission

class Study_centerPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class Study_CenterDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff
        
class TeacherPermission(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        
class TeacherDetailPermisison(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method in ['POST', 'PUT', 'DELETE']:
            return request.user.is_staff
        
class StudentPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method in ['POST', 'POST', 'DELETE']:
            return request.user.is_staff
        
class StudentDetailPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method in ['POST', 'PUT']:
            return request.user.is_staff
        