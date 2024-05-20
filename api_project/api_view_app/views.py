from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def home(request):
    if request.method =="GET":
        return Response({
            'status':200,
            'response':'API working Successfully',
            'method':'GET'
        })
    elif request.method =="POST":
        return Response({
            'status':200,
            'response':'API working Successfully',
            'method':'POST'
        })
    elif request.method =="PUT":
        return Response({
            'status':200,
            'response':'API working Successfully',
            'method':'PUT'
        })
    else:
        return Response({
            'status':200,
            'response':'API working Successfully',
            'method':'Unknown Method Called'
        })
    
    
from .serializers import TodoSerializer  
    
#Using Serializers with api_view
@api_view(['POST'])
def post_home(request):
    if request.method == "POST":
        data=request.data
        serializer=TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"Message":"The Data is Posted","Status":"Posted 200"})        
    else:
        return Response({"Message":"The Data is Not Posted","Status":"404 something went wrong"})

from rest_framework.renderers import JSONRenderer
from .models import *
#Get Request 
@api_view(['GET'])    
def get_home(request):
    if request.method == "GET": 
        stu=Todo.objects.all()
        serializer=TodoSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return Response(json_data,content_type='appliecation/json')
        
    else:
        return Response({
            'status':404,
            'response':'API Not working Successfully',
            'method':'GET',
            'error':serializer.errors
            })
        
        
#Class Based Views
from rest_framework.views import APIView

class TodoView(APIView):
    def get(self,request):
        if request.method == "GET": 
            stu=Todo.objects.all()
            serializer=TodoSerializer(stu,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return Response(json_data,content_type='appliecation/json') 
        else:
            return Response({
                'status':404,
                'response':'API Not working Successfully',
                'method':'GET'
                })
            
    def post(self,request):
        if request.method == "POST":
            data=request.data
            serializer=TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Message":"The Data is Posted","Status":"Posted 200"})        
            else:
                return Response({"Message":"The Data is Not Posted","Status":"404 something went wrong"})
            
    def patch(self,request):
        if request.method == "PATCH":
            data=request.data
            title=data.get("todo_title")     
            try:       
                obj=Todo.objects.get(todo_title=title)
                print(f"Title Present {title}")
                serializer=TodoSerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200 ,
                        'response':'API Updated Successfully',
                        'method':'PATCH'
                        })
                else:
                    return Response({
                    'status':404,
                    'response':'API Not working',
                    'error':serializer.errors})
            except Exception as e:
                print(e)
                print("Entet the Validate Title")
                return Response({
                    'status':404,
                    'response':'API Not working'})
                
                
#Creating the API Using Viewsets(most simple and fastest form to create the API)
from rest_framework import viewsets,status

class TodoViewset(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    