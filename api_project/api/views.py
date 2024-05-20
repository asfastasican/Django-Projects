from django.shortcuts import render
from .models import Student
from .serializers import *
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.    
def Student_api(request):
    if request.method == "GET":
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream=stream)
        id=pythondata.get('id',None)
        print(id)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='appliecation/json')
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='appliecation/json')
    
@csrf_exempt
def  student_create(request):
    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream=stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            print("Data is validated")
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            print("Sending the Response")
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
@csrf_exempt   
def student_partial_update(request):
    if request.method == "PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream=stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data PArtially Updated !!'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)       
@csrf_exempt    
def student_update(request):
    if request.method == "PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream=stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated ******'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)   
    
@csrf_exempt    
def student_delete(request):
    if request.method == 'DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream=stream) 
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete() 
        res={"msg":"Data is Deleted"}
        return JsonResponse(res,safe=False)