from django.contrib import admin
from .models import Student,FeedBackForm,Studentinfo

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','marks','city']
    
class FBAAdmin(admin.ModelAdmin):
    list_display=['name','rollno','email','feedback']
    
class StudentinfoAdmin(admin.ModelAdmin):
    list_display=['id','name','city']

# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(FeedBackForm,FBAAdmin)
admin.site.register(Studentinfo,StudentinfoAdmin)
