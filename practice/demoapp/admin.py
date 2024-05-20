from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display=['Name','Roll','City']
    
# Register your models here.
admin.site.register(StudentModel,StudentAdmin)




