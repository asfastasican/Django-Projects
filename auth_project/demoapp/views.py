from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

# Create your views here.

@login_required
def display(request):
    return HttpResponse("<h1>This is Home Page</h1>")

def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("Home")
    else:
        form=SignupForm()
        return render(request,'signup.html',{'form':form}) 
    
    