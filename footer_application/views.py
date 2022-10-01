from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from footer_application.models import *
from footer_application.serializers import *


class Footerviews(APIView):
    def get(self,request,*args, **kwargs):
        get_top = About.objects.all()
        webthemes =Column.objects.all()

        serializer1 =  AboutSerializer(get_top,many=True)
        serializer2 =  ColumnSerializer(webthemes, many=True)

        context={
           " status" : status.HTTP_200_OK,
           "sucess":True,
           "response1":serializer1.data,
           "response2":serializer2.data,
           
             }
        return Response(context,status=status.HTTP_200_OK)