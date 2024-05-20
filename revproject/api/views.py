from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.
#For single Model Instance
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    print(type(stu))
    print(stu)
    serializer=StudenSerializer(stu)
    print(type(serializer))
    print(serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print(type(json_data))
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')

#Query Set - All Student Data
def student_list(request):
    stu=Student.objects.all()
    serializer=StudenSerializer(stu,many=True)
    #json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)                        # Using JsonResponse insted of HTTP

#De-serialization
#for Posting the data
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudenSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Data Created'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
    
    
######################## Function Based CURD ##################################

#Reading the insgtance via API    
@csrf_exempt
def student_get(request,pk):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudenSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
        stu=Student.objects.all()
        serializer=StudenSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
            
        
        
    

