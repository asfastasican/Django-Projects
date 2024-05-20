from django.urls import path
from .views import *

urlpatterns = [
    path('welcome/',welcome),
    path('templateview/',templateview),
    path('stud_view/',stud_view),
    path('stud_form/',stud_form),
    path('stud_modelform/',stud_modelform),
    path('create_student/',create_student),
    path('update_student/<int:id>',update_student),
    path('retrive_student/',retrive_student),
    path('delete_student/<int:id>',delete_student),
    path('StudentListView/',StudentListView.as_view()),
    path('CreateStudentView/',CreateStudentView.as_view()),
    #path('UpdateStudentView/<int:id>',UpdateStudentView.as_view()),
    #path('DeleteStudentView/<int:1>',DeleteStudentView.as_view()),
    path('welcome_back/',demo_back),
    path('orm_emp/',orm_emp),
]