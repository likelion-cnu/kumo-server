from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from rest_framework.authentication import TokenAuthentication
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from .serializers import LoginSerializer, SignupSerializer, ChangePasswordSerializer, WhenLoginGiveBoolean
from .models import  User, CustomerUser
from . import models

User_all = get_user_model()

# 회원가입하고, 토큰 발행
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    authentication_classes = [TokenAuthentication]
    
# 로그인하고, 유저에 맞는 토큰 가져오기
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = [TokenAuthentication]
        
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token_user = serializer.validated_data # LoginSerializer안의 validate()의 리턴값인 Token을 받아옴
        token = token_user["token"]
        user = token_user["User"]
        request.session['user'] = user.username
        #qurey_bo = get_object_or_404(User, username=request.user.username)
        #qurey_bo = User.objects.get(username=request.user)
        serial_bo = WhenLoginGiveBoolean(user)#status=status.HTTP_200_OK
        return Response({"token": token.key, "serial_bo":serial_bo.data}, status=status.HTTP_200_OK)


# 로그아웃하고, 토큰 삭제
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    
    def get(self, request, format=None):
        # simply delete the token to force a login
        # request.user.auth_token.delete()
        if request.session.get('user'):
            del(request.session['user'])
            return Response(status=status.HTTP_200_OK)


# 비밀번호 변경
class ChangePwdView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    authentication_classes = [TokenAuthentication]
    # GenericAPIView에서 lookup_field의 역할은 update할 대상이 되는 object를 지정해준다ㅏ.
    lookup_field = 'username'

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
