from dataclasses import fields
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

# 회원가입 Serializer
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username", "password", "nickname", "phone_num", "is_shop"
        ]

    # 유효성 검사를 통과할 때
    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"], 
            nickname = validated_data["nickname"],
            phone_num = validated_data["phone_num"],
            is_shop=validated_data["is_shop"],
            )
        if user is None:
            return {"error": "Unable to log in"}     
        user.set_password(validated_data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return user


# 로그인 Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    # write_only를 통해서 서버 -> 클라이언트 방향의 직렬화를 방지하여 보안 UP
    password = serializers.CharField(required = True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return {"token":token, "User":User.objects.get(username=user.username)}         
        raise serializers.ValidationError(
            {"error": "Unable to log in"}
        )


class WhenLoginGiveBoolean(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("is_shop", "username")


# 비밀번호 변경 Serializer
class ChangePwdSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance