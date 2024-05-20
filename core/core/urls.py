"""core URL Configuration

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
from firstapp import views
from api import views as v2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Home/',views.home_view),
    url(r'^date/',views.date_time),
    url(r'^time/',views.time_module),
    url(r'^read/',views.read_view),
    url(r'^read_html/',views.read_view_html),
    url(r'^form/',views.form_view),
    url(r'^feedback/',views.feedback_view),
    url(r'^student_api/<int:pk>',views.student_api_info),
    url(r'student_api_list/',views.student_api_list),
    url(r'^api_single/<int:pk>',views.api_single),
    url(r'api_list/',views.api_list),
    url(r'car_api/<int:pk>',v2.car_api_info),
    url(r'car_api_list/',v2.car_api_list),
    
]
