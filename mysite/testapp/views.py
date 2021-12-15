from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView

from .models import students
from .serializers import studentsSerializer




# Create your views here.

class studentList(ListAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializer


class getOnlyStudent(RetrieveAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializer


class createStudent(CreateAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializer


class updateStudent(UpdateAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializer


class deleteStudent(DestroyAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializer
