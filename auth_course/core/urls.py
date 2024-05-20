from django.urls import path
from core.views import RegisterView,Loginview,UserApiView

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',Loginview.as_view()),
    path('user',UserApiView.as_view()),
    ]
