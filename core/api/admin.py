from django.contrib import admin
from .models import Car_info

# Register your models here

class Car_info_Admin(admin.ModelAdmin):
    list_display=['id','name','country']
    
admin.site.register(Car_info,Car_info_Admin)