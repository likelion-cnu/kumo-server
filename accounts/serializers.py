from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    
    # 유효성 검사를 통과할 때
    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"], 
            is_shop=validated_data["is_shop"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = [
            "username", "password", "phone_num", "is_shop"
        ]

