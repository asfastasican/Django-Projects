from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
    
@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display=['emp_id','name','department','city','company']

    