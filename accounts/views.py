from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from .serializers import SignupSerializer
from .models import  User, CustomerUser
from . import models

import qrcode


# Create your views here.

# 회원가입하고, 토큰 발행
class SignupView(APIView):
    def post(self, request):
        username=request.data['username']
        user = User.objects.create_user(username=username, 
                                        password=request.data['password'],
                                        phone_num=request.data['phone_num'],
                                        is_shop=request.data['is_shop'],                               
                                        )
        user.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key})


# 로그인하고, 유저에 맞는 토큰 가져오기
class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)        
            return Response({"Token": token.key})
        else:
            return Response(status=401)


class LogoutView(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)







# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         search_username = data['username']
#         obj = User.objects.get(username=search_username)

#         if data['password'] == obj.password:
#             return HttpResponse(status=200)
#         else:
#             return HttpResponse(status=400)

