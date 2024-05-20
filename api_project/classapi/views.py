from django.shortcuts import render
from .models import Student
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.    
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #authentication_classes=[BaseAuthentication]
    #permission_classes=[IsAuthenticated]
