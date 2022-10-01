from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from navbar_application.models import *
from navbar_application.serializers import *


class WebThemes(APIView):
    def get(self,request,*args, **kwargs):
        get_top = Topsection1.objects.all()
        webthemes =Topsection2.objects.all()

        serializer1 = Topsection1Serializer(get_top,many=True)
        serializer2 =Topsection2Serializer(webthemes, many=True)

        context={
           " status" : status.HTTP_200_OK,
           "sucess":True,
           "response1":serializer1.data,
           "response2":serializer2.data,
           
             }
        return Response(context,status=status.HTTP_200_OK)
