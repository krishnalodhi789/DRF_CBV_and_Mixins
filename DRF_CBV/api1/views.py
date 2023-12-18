from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
class StudentListView(APIView):
    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context={
                    "success":True,
                    "status": status.HTTP_201_CREATED,
                    "data":serializer.data
                }
                return Response(context)
        except Exception as error:
            context={
                    "success":True,
                    "status": status.HTTP_404_NOT_FOUND,
                    "data":str(error)
                }
            return Response(context)
    
    def get(self, request):
        try:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many = True)
            context={
                "success":True,
                "status": status.HTTP_200_OK,
                "data":serializer.data
            }
            return Response(context)
        except Exception as error:
            context={
                "success":True,
                "status": status.HTTP_404_NOT_FOUND,
                "data":str(error)
            }
            return Response(context)
        
class GetStudentUpdateAndDelete(APIView):
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            context = {
                "success":True,
                "status":status.HTTP_200_OK,
                'data':serializer.data
            }
            return Response(context)
        except Exception as error:
            context = {
                "success":True,
                "status":status.HTTP_404_NOT_FOUND,
                'data':str(error)
            }
            return Response(context)
        
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student ,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                context = {
                    "success":True,
                    "status":status.HTTP_205_RESET_CONTENT,
                    'data':serializer.data
                }
                return Response(context)
        except Exception as error:
            context = {
                "success":True,
                "status":status.HTTP_404_NOT_FOUND,
                'data':str(error)
            }
            return Response(context)
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            context = {
                "success":True,
                "status":status.HTTP_200_OK,
            }
            return Response(context)
        except Exception as error:
            context = {
                "success":True,
                "status":status.HTTP_404_NOT_FOUND,
                'data':str(error)
            }
            return Response(context)
        