"""templateproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from demoapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/',views.tempview),
    url(r'^emp/',views.emp),
    url(r'^empform/',views.EmpForm),
    url(r'^empmf/',views.emp_model_form),
    url(r'^ret/',views.ret_create,name="list"),
    url(r'^posting/',views.posting,name="posting"),
    url(r'^del/(?P<id>\d+)/',views.emp_delete),
    url(r'^up/(?P<id>\d+)/',views.emp_update),
    url(r'^classlist',views.HelloWorldView.as_view()),
    url(r'^sel/',views.selenium_func),
    url(r'^ss/',views.selenium_screenshot),  
    url(r'^soup/',views.b_soup), 
]

