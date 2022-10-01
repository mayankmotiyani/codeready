from rest_framework import serializers
from navbar_application.models import *


class TopsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topsection
        fields = '__all__'

class Topsection1Serializer(serializers.ModelSerializer):
    topsection = serializers.StringRelatedField()
    class Meta:
        model = Topsection1
        fields =  '__all__'

class Topsection2Serializer(serializers.ModelSerializer):
    topsection = serializers.StringRelatedField()
    topsection1 = serializers.StringRelatedField()
    class Meta:
        model = Topsection2
        fields =  '__all__'