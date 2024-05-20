from django.urls import path
from .views import *

urlpatterns = [
    path('api/get-hotels/',get_hotels),
]