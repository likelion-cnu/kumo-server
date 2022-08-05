from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from .serializers import LoginSerializer, SignupSerializer, ChangePwdSerializer
from .models import  User, CustomerUser
from . import models



# 회원가입하고, 토큰 발행
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


# 로그인하고, 유저에 맞는 토큰 가져오기
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data # LoginSerializer안의 validate()의 리턴값인 Token을 받아옴
        return Response({"token": token.key}, status=status.HTTP_200_OK)


# 로그아웃하고, 토큰 삭제
class LogoutView(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# 비밀번호 변경
class ChangePwdView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePwdSerializer
    # GenericAPIView에서 lookup_field의 역할은 update할 대상이 되는 object를 지정해준다ㅏ.
    lookup_field = 'username'


    def get_queryset(self):
        user = User.objects.filter(username=self.request.user.username)
        qs = super().get_queryset()
        # 장고의 in은 튜플, 리스트, 쿼리셋 등 반복 가능한 객체를 조회한다. SQL문에서의 WHERE IN과 같은 역할을 한다.
        qs = qs.filter(username__in=user)
        return qs

