from django.urls import path
from .views import *

urlpatterns = [
    path('set_cookies/',set_cookies),
    path('get_cookies/',get_cookies),
    path('del_cookies/',del_cookie),
    path('set_signed_cookies/',set_signed_cookies),
    path('get_signed_cookies/',get_signed_cookies)
]