from django.contrib import admin
from demoapp.models import Student
from demoapp.models import Employee
from demoapp.models import Demo

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','salary','address']

class DemoAdmin(admin.ModelAdmin):
    list_display=['id','name']
    
admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Demo,DemoAdmin)
