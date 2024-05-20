from django.shortcuts import render
from .models import Car_info
from .serializers import Car_infoSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.
def car_api_info(request,pk):
    cr=Car_info.objects.get(id=pk)
    serlizer=Car_infoSerializer(cr)
    json_data=JSONRenderer().render(serlizer.data)
    return HttpResponse(json_data,content_type='application/json')


def car_api_list(request):
    cr=Car_info.objects.all()
    serlizer=Car_infoSerializer(cr,many=True)
    return JsonResponse(serlizer.data)
    
    
    



