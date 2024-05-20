from django.contrib import admin
from django.urls import path,include
from api import views
from classapi import views as classviews
from rest_framework.routers import DefaultRouter
from api_view_app import urls as u2 



router=DefaultRouter()
router.register('studentapi', classviews.StudentModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api_view/',include(u2)),
    path('studentapi/',views.Student_api),
    path('stucreate/',views.student_create),
    path('stupatch/',views.student_partial_update),
    path('stupdate/',views.student_update),
    path('studel/',views.student_delete),
]