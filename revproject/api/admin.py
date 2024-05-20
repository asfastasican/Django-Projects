from django.contrib import admin
from.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

# Register your models here.
admin.site.register(Student,StudentAdmin)