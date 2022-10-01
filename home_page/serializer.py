from rest_framework import serializers
from home_page.models import Category,Banner

class CategorySerializer(serializers.ModelSerializer):
    cat_title = serializers.StringRelatedField()
    total_sales = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['title','id','image','heading','discription','price','sales']

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
