from django.urls import path
from .views import *

urlpatterns = [
    path("student_detail/<int:pk>",student_detail),
    path("student_list/",student_list),
    path("student_create/",student_create),
    path("student_get/",student_get),
]
