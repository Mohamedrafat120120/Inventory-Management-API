from django.shortcuts import render
from .models import MyUser
from .serializers import register_serializer,login_serializer,profile_serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework.response import Response
# Create your views here.

class register(APIView):
    def post(self, request):
        if not MyUser.objects.filter(request.user).exists():
          serializer = register_serializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
class login(APIView):
    def  post(self,request):
        serialize=login_serializer(data=request.data)
        if serialize.is_valid():
            email=serialize.data.get('email')
            password=serialize.data.get("password")
            user=authenticate(username=email,password=password)
            if user:
                request_User=MyUser.objects.get(email=serialize.data.get('email'))
                user_serialize=profile_serializer(request_User)
                return Response({"msg":"login success","user":user_serialize.data},status=status.HTTP_200_OK)
            else:
                return Response({"msg":"user not found"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serialize.errors)
        
        
        
        
        
class profile(APIView):
    def get(self,request):
        user=request.user
        if user is not None:
         user_serialize=profile_serializer(user)
         return Response({"user":user_serialize.data},status=status.HTTP_200_OK)
        else:
            return Response({"error":"user not found"},status=status.HTTP_404_NOT_FOUND)