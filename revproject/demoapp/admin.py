from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','marks']
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empno','name','age','salary','address']

# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)

