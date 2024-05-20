from django.contrib import admin
from .models import *


class AmenitiesAdmin(admin.ModelAdmin):
    list_display=['amenity','created_at','updated_at']
    
class HotelAdmin(admin.ModelAdmin):
    list_display=['hotel_name','hotel_price','hotel_description','banner_image','created_at','updated_at']
    
class HotelImageAdmin(admin.ModelAdmin):
    list_display=['hotel','image','created_at','updated_at']

# Register your models here.
admin.site.register(Amenities,AmenitiesAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(HotelImage,HotelImageAdmin)
