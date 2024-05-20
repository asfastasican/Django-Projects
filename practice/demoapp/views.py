from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def demo_view(request):
    return HttpResponse("<h1>This is a demo function</h1>")

def list_view(request):
    obj=StudentModel.objects.all()
    my_dict={"stud_list":obj}
    return render(request,template_name="demo_list.html",context=my_dict)

def create_stud(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(f'<h1>Student Created Successfully</h1>')
    else:
        form=StudentForm()
        return render(request=request,template_name="create_stud.html",context={"form":form})
    
def delete_stud(request,id):
    stud=StudentModel.objects.get(id=id)
    stud.delete()
    return redirect()    