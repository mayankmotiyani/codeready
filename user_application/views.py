from django.shortcuts import render
from django.http import HttpResponse
from user_application.models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from user_application.serializer import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserRegister(APIView):
    def get(self,request):
        try:
       
            get_user = CustomUser.objects.all()   #filter(id=id)
            print(get_user)
            serializer = CustomUserSerializer(get_user,many=True)
            
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
            }
            return Response(context,status=status.HTTP_302_FOUND)
        except Exception as exception:
       
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "message":"invalid credentials"
            }
            return Response(context,status=status.HTTP_404_NOT_FOUND)
       
    def post(self , request ):
        
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            context ={
                "status": status.HTTP_200_OK,
                "success":True,
                "message":"user registered successfully"
            }

            return Response(context,status=status.HTTP_200_OK)
        
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
# class UserLogin(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     # def get(self , request ):
#     #     pass

#     def post(self,request):
#         serializer = CustomUserSerializer(data= request.data)

#         if serializer.is_valid():
#             user = CustomUser.objects.get(email=serializer.data['email'],password=serializer.data['password'])
#             refresh = RefreshToken.for_user(user)
#             login(request, user)


#             context = {
#                 "status":status.HTTP_200_OK,
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#             }
#             return Response(context,status=status.HTTP_302_FOUND)
        

#         return Response(context,status=status.HTTP_404_NOT_FOUND)
       

        

        