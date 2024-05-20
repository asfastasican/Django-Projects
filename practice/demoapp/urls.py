from django.urls import path
from .views import *

urlpatterns = [
    path('demo/',demo_view),
    path('list/',list_view),
    path('create/',create_stud),
]