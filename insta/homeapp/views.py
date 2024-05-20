from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def home(request):
    
    """
     Logic
    
    """
    
    #return render(request,html)
    return HttpResponse("<h1>Hello welcome to Instagram Home</h1>")