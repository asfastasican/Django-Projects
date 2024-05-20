from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'todo-view-set',TodoViewset,basename='todo')

urlpatterns = [
    path('home/',home),
    path('post_home/',post_home),
    path('get_home/',get_home),
    path('todoview/',TodoView.as_view()),
]

urlpatterns+=router.urls