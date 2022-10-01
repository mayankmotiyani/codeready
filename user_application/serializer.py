from rest_framework import serializers
from user_application.models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



   
    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            # last_login=validated_data['last_login'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password = make_password(validated_data['password']),
        )
        return user
    
    

    def validate_email(self, value):
        # em = data['email'][0]

        if '_'in value[0] or '-' in value[0] :#or value[0].isdigit()
            raise serializers.ValidationError({"error":"enter a valid email address"})

        return value

    def validate_username(self,value):

        if value != value.lower() or value[0].isdigit():
            raise serializers.ValidationError({"error":"Username must be in lower case or username should not start with numeric values "})

        return value

    def validate_password(self, value):
        if len(value) < 6 :
            raise serializers.ValidationError({"error":"Password should be at least 6 characters"})

        return value
