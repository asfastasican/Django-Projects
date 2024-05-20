from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
HttpResponse.set_cookie("name",                      #key
                        "Akshay",                    #Value                
                        max_age=60*60*24*10,         #age of cookie in seconds or None(It expires with brower closing)
        expires=datetime.utcnow()+timedelta(days=2)  #used for deleting the cookies 
                        path"/"                      #Defaullt is root can store our cookies in specific location
                        domin="xyx.com"              #This cookie will be accessibe for xyx.com
                        secure=True                  #This will run only on https/ secure connection only 
                           
                        )
"""


def set_cookies(request):
    response=HttpResponse("<h1>Cookie Ceated Sucessfully</h1>")
    response.set_cookie("lname","Akshay Laxman Shelke")
    return response

def get_cookies(request):
    #name=request.COOKIES['lname']
    name=request.COOKIES.get("lname")
    if name :
        return HttpResponse(f"<h1> Name is {name} <h1>")
    else :
        return HttpResponse("<h1> Name is not available <h1>")
    
def del_cookie(request):
    response=HttpResponse("<h1>Cookie Deleted</h1>")
    response.delete_cookie("lname")
    return response
    
    
def set_signed_cookies(request):
    response=HttpResponse("<h1>Cookie Ceated Sucessfully</h1>")
    response.set_signed_cookie("City","Baramati",salt="nm")
    return response

def get_signed_cookies(request):
    #name=request.COOKIES['lname']
    name=request.get_signed_cookie("City",salt="nm",default="Rinzler")
    if name :
        return HttpResponse(f"<h1> Name is {name} <h1>")
    else :
        return HttpResponse("<h1> Name is not available <h1>")