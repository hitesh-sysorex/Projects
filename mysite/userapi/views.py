from django.shortcuts import render


from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView

from .models import userData
from .serializers import userDataSerializer

# Create your views here.

class userList(ListAPIView):
    queryset = userData.objects.all()
    serializer_class = userDataSerializer

class getOnlyUser(RetrieveAPIView):
    queryset = userData.objects.all()
    serializer_class = userDataSerializer

class createUser(CreateAPIView):
    queryset = userData.objects.all()
    serializer_class = userDataSerializer

class updateUser(UpdateAPIView):
    queryset = userData.objects.all()
    serializer_class = userDataSerializer

class deleteUser(DestroyAPIView):
    queryset = userData.objects.all()
    serializer_class = userDataSerializer