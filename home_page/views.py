from django.shortcuts import render
from django.http import HttpResponse
from home_page.models import Category,Banner
from rest_framework.response import Response
from rest_framework.views import APIView
from home_page.serializer import CategorySerializer,BannerSerializer
from rest_framework import status



# Create your views here.

class ProductCategory(APIView):
    
    def get(self,request,*args, **kwargs):
        product = True
        search = request.GET.get('heading')
        price = request.GET.get('price')

        if search:
            product = Category.objects.filter(heading__icontains=search)
            serialize = CategorySerializer(product,many=True)

        else:
             product =  Category.objects.all()
             serialize = CategorySerializer(product,many=True)

         
        product_cat =  Category.objects.all().order_by('-price')
        serialize1 = CategorySerializer(product_cat,many=True)

    
        product_cat =  Category.objects.all().order_by('price')
        serialize2 = CategorySerializer(product_cat,many=True)
    
        content = {
            "status":status.HTTP_200_OK,
            "success":True,

            "response":serialize.data,
            "response1": serialize1.data,
            "response2": serialize2.data,
            
        }

        return Response(content,status=status.HTTP_200_OK)

class HomeBanner(APIView):

    def get(self,request,*args, **kwargs):
        get_all = Banner.objects.all()
        serialize = BannerSerializer(get_all,many=True)
        content = {
            "status":status.HTTP_200_OK,
            "success":True,
            "response":serialize.data
        }
        
        return Response(content,status=status.HTTP_200_OK)
