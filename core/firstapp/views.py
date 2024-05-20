from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import datetime
from .models import Student,Studentinfo
from .forms import StudentForm,FeedbackForm
from .serializers import StudentSerializer,StudentinfoSerizalizer
from rest_framework.renderers import JSONRenderer


# Create your views here.

def home_view(request):
    return HttpResponse('<h1>This is a Home page</h1>')   

def date_time(request):
    t=str(datetime.datetime.now())
    return HttpResponse(f'<h1>{t}</h1>')

def time_module(request):
    time=str(datetime.datetime.now())
    my_dict={'date_msg':time}
    return render(request,'firstapp/home.html',context=my_dict)

def read_view(request):
    stud=Student.objects.all()
    print(stud)
    return HttpResponse("<h>This is a Read View</h>")    

def read_view_html(request):
    stud=Student.objects.all()
    my_dict={'stud_list':stud}
    return render(request,'firstapp/read.html',context=my_dict) 

def form_view(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            passwords=form.cleaned_data['password']
            up=name.upper()
            print(up)
            print(passwords)
            return HttpResponse(f'<h1>Form sucessfully submited {up}</h1>') 
    else:
        form=StudentForm()
        context={'form':form}       
    return render(request,'firstapp/form.html',context=context)

def feedback_view(request):
    if request.method == "POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('<h1>saved sucesfully<h1>')
    else:
        form=FeedbackForm()
        context={'form':form}
    return render(request,'firstapp/feedback.html',context=context)


def student_api_info(request,pk):
    stu=Student.objects.get(id=pk)  #getting the instance
    serializer=StudentSerializer(stu)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=True)
    
def student_api_list(request):
    stu=Student.objects.all()  #getting all the data
    print(stu)
    serializer=StudentSerializer(stu)
    print(serializer.data)
    data=JSONRenderer().render(serializer.data)
    print(data)
    return HttpResponse(data)

def api_single(request,pk):
    stu=Studentinfo.objects.get(id=pk)  #getting the instance
    serializer=StudentinfoSerizalizer(stu)  #Converting to python Object
    json_data=JSONRenderer().render(serializer.data)  #Conveting to JSON
    return HttpResponse(json_data,content_type='application/json')
    
def api_list(request):
    stu=Studentinfo.objects.all()  #getting all the data
    serializer=StudentinfoSerizalizer(stu,many=True)
    data=JSONRenderer().render(serializer.data)
    return HttpResponse(data)

