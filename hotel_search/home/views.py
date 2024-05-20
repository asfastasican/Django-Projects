from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def get_hotels(request):
    try:
        hotel_objs=Hotel.objects.all()
        
        if request.GET.get('sort_by'):     #Code For Sorting the Hotel Prices
            sort_by_value=request.GET.get('sort_by')
            if sort_by_value == 'asc':
                print('ASC worked')
                hotel_objs=hotel_objs.order_by('hotel_price')
            elif sort_by_value == 'dsc':
                print('DSC worked')
                hotel_objs=hotel_objs.order_by('-hotel_price')
        
        if request.GET.get('amount'):
            amount=request.GET.get('amount')
            hotel_objs=hotel_objs.filter(hotel_price__ltr=amount)
                
        payload=[]
        for hotel_obj in hotel_objs:
            payload.append({
                'hotel_name': hotel_obj.hotel_name,
                'hotel_price': hotel_obj.hotel_price,
                'hotel_description': hotel_obj.hotel_description,
                'banner_image': str(hotel_obj.banner_image),                   
                })
        return JsonResponse(payload,safe=False)   
    except Exception as e:
        print(e)
    return JsonResponse({'Message':'Something Wrong'})