from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissons import IsShop
# Create your views here.


# 루트 페이지에 로그인 되어있는지와 업주 유저인지 확인
class RootView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
    pass   



# QR 체크하고, 고객의 쿠폰의 스탬프 개수를 올리는 뷰 // POST, UPDATE
class CheckQrView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
    pass   


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
class MyShopView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    permission_classes = [IsShop]
    pass   


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