from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import UserSerializer
from rest_framework.exceptions import APIException,AuthenticationFailed
from core.models import User
from core.authentication import create_access_token,create_refresh_token,decode_access_token
from rest_framework.authentication import get_authorization_header

# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        data=request.data
        if data.get("password")!=data.get("password_confirm"):
            raise APIException("Passwords are not matching")
        serializer=UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(request.data)
        else:
            return Response(serializer.errors)
        
        
#Creating the class for Login
class Loginview(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user=User.objects.filter(email=email).first()
        
        #Validating the User
        if user is None:
            raise AuthenticationFailed("Invalid Credientials")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid Credentials")
        
        access_token=create_access_token(user.id)
        refresh_token=create_refresh_token(user.id)        
        response=Response()
        response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
        response.data={'token':access_token}  #sending the access token as response
        return response

class UserApiView(APIView):
    def get(self,request):
        auth=get_authorization_header(request=request).split()
        if auth and len(auth) == 2:
            token=auth[1].decode('utf-8')
            print(token)
            print(auth[0])
            user_id=decode_access_token(token)
            user=User.objects.get(pk=user_id)
            if user:
                serializer=UserSerializer(user)
                return Response(serializer.data)
        else:
            raise AuthenticationFailed("Unauthenticated")