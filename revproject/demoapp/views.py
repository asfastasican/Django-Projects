from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime

# Create your views here.

#this view for just running the simple http response
def welcome(request):
    return HttpResponse(f"<h1>Welcome to Home Page {datetime.datetime.now()}</h1>")

#this view for linking to template and sending context to home page
def templateview(request):
    context={'datetime':datetime.datetime.now()}
    return render(request,'demoapp/wish.html',context=context)

#this view will load all the data from model
from .models import Student

def stud_view(request):
    stud_list=Student.objects.all()
    my_dict={'stud_list':stud_list}
    return render(request,'demoapp/student.html',context=my_dict)

#this view is for forms 
from .forms import StudentForm,StudentModelForm

def stud_form(request):
    form=StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['marks'])
            
    else:
        form=StudentForm()
    return render(request,"demoapp/studentform.html",context={'form':form})


#this view is for student modelform
def stud_modelform(request):
    if request.method == 'POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'demoapp/wish.html')
    else:
        form=StudentModelForm()
    return render(request,"demoapp/studentform.html",context={'form':form})


### Function based Curd Operations

#create 
def create_student(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/demoapp/stud_view")
    else:
        form=StudentForm()
    return render(request,"demoapp/studentform.html",context={'form':form})

#update
def update_student(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentModelForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("/demoapp/stud_view")
    else:
        form=StudentModelForm()
    return render(request,"demoapp/studentform.html",context={'form':form})

#Retrive
def retrive_student(request):
    stud_list=Student.objects.all()
    my_dict={'stud_list':stud_list}
    return render(request,'demoapp/student.html',context=my_dict)

#Deleting

def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("/demoapp/stud_view")
    
    
    
######################   Class Based Views   ########################
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

#class view for Retrive all Records
class StudentListView(ListView):
    model=Student
    template_name="demoapp/student.html"
    
#Create View
class CreateStudentView(CreateView):
    model=Student
    fields="__all__"
    template_name="demoapp/studentform.html"
    
#Update View
class UpdateStudentView(UpdateView):
    model=Student
    fields=('name','marks')
    template_name="demoapp/studentform.html"
    success_url="demoapp/stud_view"
    
#Delete View 
class DeleteStudentView(DeleteView):
    model=Student
    fields=('name','marks')
    template_name="demoapp/studentform.html"
    success_url="demoapp/stud_view"
    
    
    
#######################   ORM    ########################

from .models import Employee

def orm_emp(request):
    emps=Employee.objects.all()                      #All objects
    emps=Employee.objects.filter(salary__gt=70000)   #Greater Than 
    emps=Employee.objects.filter(salary__gte=70000)  #Greater Than Equal to 
    emps=Employee.objects.filter(salary__lt=70000)   #Less Than 
    emps=Employee.objects.filter(salary__lte=45000)  #Less Than Equal to
    emps=Employee.objects.get(name__exact="Akshay")  #Geting one Object
    emps=Employee.objects.filter(name__contains="na") 
    print(type(emps))
    print(emps)
    #e=Employee(empno=12,name="Jui",age=3,salary=2000,address="Baramati")
    #e.save()
    emps=Employee.objects.filter(name__iexact="jui")
    if emps:
        print(emps)
    return HttpResponse("<h1>ORM Executed Sucessfully</h1>")


def demo_back(request):
    return HttpResponse("<h1>Welcome Back Rinzler</h1>")
