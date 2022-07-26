from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status

from accounts.permissons import IsShop
from accounts.models import User, CustomerUser, ShopUser

from .serializers import ShopUserSerializer, QRcodeSerializer
from .models import Coupon

# 루트 페이지에 로그인 되어있는지와 업주 유저인지 확인
class RootView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
    pass   


# QR 체크하고, 고객의 쿠폰의 스탬프 개수를 올리는 뷰 // POST, UPDATE
class Check_QRcodeView(APIView):
    def post(self, request):
        serializer = QRcodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def put(self, request):
        coupon = Coupon.objects.filter(writer = request.data['writer']
                                    #   shopname = request.data['shopname']
                                      )
        coupon.save()
        return Response(status=status.HTTP_200_OK)





def check_QRcode(self, request):
    coupon = get_object_or_404(Coupon, writer=request.writer, shopname=request.shopname)

    if request.method == 'GET':
        serializer = QRcodeSerializer(coupon)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QRcodeSerializer(coupon, data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.writer , shopname=request.shopname)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        coupon.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 결제 정보를 등록하는 뷰 // POST
class PaymentView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
    pass   


# 업체 프로필에 접근하고 업주 유저인지 확인
class ProfileView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
    pass   



# 내 가게에 접근하고 업주 유저인지 확인
class MyShopViewSet(ModelViewSet):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
   
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer



# 내 가게 데이터에 접근하고 업주 유저인지 확인
class ShopdataView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
    pass   


# 업주 QNA에 접근하고 업주 유저인지 확인
class ShopQnaView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
    pass   