from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Employee
from .forms import EmpForm,EmpModelForm
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import View


# Create your views here.
def tempview(request):
    my_dict={"time":datetime.datetime.now()}
    return render(request,'demoapp/hello.html',context=my_dict)

#This is a Checkpoint for diff
#This I am changing on GitHub

def emp(request):
    emp_list=Employee.objects.all()
    #emp_list=Employee.objects.filter(salary__gte=20)  greater than equal to
    #emp_list=Employee.objects.filter(salary__lt=20)   less than 
    #emp_list=Employee.objects.filter(salary__lte=20)   # less than equal to 
    #emp_list=Employee.objects.get(address__exact='pune')
    #emp_list=Employee.objects.filter(name__contains='jim') #just like like in sql
    #emp_list=Employee.objects.filter(id__in=[1,5])   #membership operator
    #emp_list=Employee.objects.filter(salary__range=(20,40))  # rang function
    #emp_list=Employee.objects.filter(salary__range=(20,40))
    #emp_list=Employee.objects.all().order_by('-salary')  #descending order
    emp_list={'emp_list':emp_list} 
    print(type(emp_list))
    print(emp_list)
    return render(request,'demoapp/emp.html',context=emp_list)

def empform(request):
    if request.method == 'POST':
        form=EmpForm(request.post)
        if form.is_valid():
            print(form.cleaned_data['id'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['salary'])
            print(form.cleaned_data['address'])
            return HttpResponse('<h1>form data inserted</h1>')
    
        form=EmpForm()
    return render(request,"demoapp/empform.html",{'form':form})


def emp_model_form(request):
    if request.method == 'POST':
        emp_form=EmpModelForm(request.POST)
        if emp_form.is_valid():
            emp_form.save(commit=True)
            return HttpResponse('<h1> The Data is Saved</h1>')
    else:
        emp_form=EmpModelForm()
        context={'form':emp_form}
    return render(request,'demoapp/EmpModelForm.html',context)

def ret_create(request):
    emp=Employee.objects.all()
    context={'emp':emp}
    return render(request,'demoapp/ret.html',context)

def posting(request):
    if request.method=='POST':
        form=EmpModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/ret")
    else:
        form=EmpModelForm()
    context={'form':form}
    return render(request,'demoapp/EmpModelForm.html',context)

def emp_delete(request,id):
    emp_obj=Employee.objects.get(id=id)
    emp_obj.delete()
    return HttpResponse("<h1>Record Deleted</h1>")

def emp_update(request,id):
    emp=Employee.objects.get(id=id)
    print("API clicked")
    if request.method=='POST':
        form=EmpModelForm(request.POST,instance=emp)
        print("Inside Post")
        print(form.errors)
        if form.is_valid():
            form.save(commit=True)
            print("Sucessfully commited")
            return HttpResponse('<h1>The update is done</h1>')
    context={'emp':emp}
    return render(request,'demoapp/update.html',context)
    
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This is the get uisng class based views</h1>')

###########>>>>>                                    ##########>>>>>>>
           #########>>>>>    Selenium    #############
###########>>>>>                                    ##########>>>>>>
     
from .Automation import base,screen_shot
def selenium_func(request):
    #url='https://unsplash.com/'
    url='https://rahulshettyacademy.com/AutomationPractice/'
    base(url)
    return HttpResponse('<h1>In side the Selenium function</h1>')

def selenium_screenshot(request):
    url='https://unsplash.com/'
    screen_shot(url)
    return HttpResponse('<h1>Screen Shot took sucessfully</h1>')

   
###########>>>>>                                      ##########>>>>>>>
           #########>>>>>    beautiful soup   <<<<<#############
###########>>>>>                                      ##########>>>>>>

from .scraping import scraping_func

def b_soup(request):
    url="https://codewithharry.com"
    obj1=scraping_func(url)
    return HttpResponse(f'<h1>Inside the BS4 ---- {obj1}----</h1>')
