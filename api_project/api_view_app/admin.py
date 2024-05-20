from django.contrib import admin
from .models import *

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=['todo_title','todo_description','is_done']
    
admin.site.register(Todo,TodoAdmin)