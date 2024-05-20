from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def welcome(request):
    s="<h1>Welcome to Framework</h1>"
    return HttpResponse(s)


def timeinfo(request):
    date=datetime.datetime.now()
    message='<h2>Now Server time is '+str(date)+' </h2>'
    return HttpResponse(date)
