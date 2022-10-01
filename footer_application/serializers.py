from rest_framework import serializers
from footer_application.models import *


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class FooterHeadingSerializer(serializers.ModelSerializer): 
  
    class Meta:
        model = FooterHeading
        fields =  '__all__'

class ColumnSerializer(serializers.ModelSerializer):
    heading= serializers.StringRelatedField()
    class Meta:
        model =Column
        fields =  '__all__'