from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.decorators import action

from accounts.permissons import IsShop
from accounts.models import User, CustomerUser, ShopUser

from .serializers import ShopUserSerializer, QRcodeSerializer, PaymentSerializer, ReviewSerializer, ReviewCommentSerializer ,ShopProfileUserSerializer, ShopProfileEditSerializer, CouponeSerializer
from .models import Coupon, Payment, Review, Review_Comment


# 루트 페이지에 로그인 되어있는지와 업주 유저인지 확인
class RootView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    #permission_classes = [IsShop]
    pass


# QR 체크하고, 고객의 쿠폰의 스탬프 개수, 유저 레벨, 결제 정보를 올리는 뷰 // POST, UPDATE
@api_view(['GET'])
def Coupon_add(request, user):
    cu = CustomerUser.objects.get(user=user)
    shop = ShopUser.objects.get(user=request.user.username)
    coupons =  Coupon.objects.filter(writer=cu, shopname=shop)
    if coupons:
        if request.method == 'GET':
            for coupon in coupons:
                coupon.save()
            Payment.objects.create(writer=cu, shopname=shop)
            return Response(status=201)
    else:    
        if request.method == 'GET':
            Coupon.objects.create(writer=cu, shopname=shop, shop_name=shop.shop_name, shop_sector=shop.shop_sector, shop_logo=shop.shop_logo)
            Payment.objects.create(writer=cu, shopname=shop)
            return Response(status=201)


# @api_view(['PUT'])
# def Coupon_put(request, user):
#     if request.method == 'PUT':
#         cu = CustomerUser.objects.get(user=user)
#         # self.kwargs.get('user')은 url에 넘겨진 인자를 가져온다.
#         shop = ShopUser.objects.get(user=request.user.username)
        
#         coupon = Coupon.objects.get(writer=cu, shopname=shop)
#         coupon.save()
#         Payment.objects.create(writer=cu, shopname=shop)
#         return Response(status=201)


# class Check_QRcodeViewSet(viewsets.ViewSet):
#     #permission_classes = [IsShop]
#     queryset = Coupon.objects.all()
#     serializer_class = CouponeSerializer

#     def create(self, request):
#         Coupon.objects.create()
#         payment_serializer = PaymentSerializer(data=request.data)
#         if payment_serializer.is_valid():
#             payment_serializer.save()
#             return Response(payment_serializer.data, status=201)


#     def update(self, request):
#         coupon = get_object_or_404(Coupon, writer=request.data['writer'], 
#                                         shopname=request.user.username)
#         coupon.save()
        
#         user_level = get_object_or_404(CustomerUser, user=request.data['writer'])
#         user_level.save()

#         review_serializer = PaymentSerializer(data=request.data)
#         if review_serializer.is_valid():
#             review_serializer.save()
            
#         return Response(status=status.HTTP_200_OK)
       


# 업체 프로필에 접근하고 업주 유저인지 확인
class ProfileViewSet(viewsets.ViewSet):
    # 업주만 접근 가능하게 permissoin 설정
    #permission_classes = [IsShop]
    
    def list(self, request): 
        queryset = Payment.objects.filter(shopname=self.request.user.username)
        serializer = PaymentSerializer(queryset, many=True)
        
        queryset2 = ShopUser.objects.filter(user=self.request.user.username)
        serializer2 = ShopProfileUserSerializer(queryset2, many=True)
        
        return Response(serializer.data + serializer2.data)



# 내 가게에 접근하고 업주 유저인지 확인
class MyShopViewSet(viewsets.ModelViewSet):
    # 업주만 접근 가능하게 permissoin 설정
    #permission_classes = [IsShop]
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    

    def list(self, request, *args, **kwargs):    
        queryset = ShopUser.objects.filter(user=self.request.user.username)
        serializer = ShopUserSerializer(queryset, many=True)
        
        review = Review.objects.filter(shopname=self.request.user.username)
        rev_serializer = ReviewSerializer(review, many=True)
        
        return Response(serializer.data + rev_serializer.data)


    @action(detail=False, methods=['POST']) 
    def create_comment(self, request):
        serializer = ReviewCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    

    def get_queryset(self):
        user = ShopUser.objects.filter(user=self.request.user)
        qs = super().get_queryset()
        # 장고의 in은 튜플, 리스트, 쿼리셋 등 반복 가능한 객체를 조회한다. SQL문에서의 WHERE IN과 같은 역할을 한다.
        qs = qs.filter(user__in=user)
        return qs



# 내 가게 데이터에 접근하고 주 유저인지 확인
class ShopdataView(ReadOnlyModelViewSet):
    # 업주만 접근 가능하게 permissoin 설정
    #permission_classes = [IsShop]
    
    queryset = Payment.objects.all()
    serializer_class = ReviewSerializer
    
    def list(self, request, *args, **kwargs):
        payment_queryset = Payment.objects.filter(shopname=self.request.user.username)
        payment_serializer = PaymentSerializer(payment_queryset, many=True)
        
        coupone_queryset = Coupon.objects.filter(shopname=self.request.user.username)
        coupone_serializer = CouponeSerializer(coupone_queryset, many=True)
        return Response(payment_serializer.data + coupone_serializer.data)

        
       
class ChangeProfileView(generics.UpdateAPIView):
    # 업주만 접근 가능하게 permissoin 설정
    #permission_classes = [IsShop]
    queryset = ShopUser.objects.all()
    serializer_class = ShopProfileEditSerializer

    lookup_field = 'user'

    def get_queryset(self):
        user = ShopUser.objects.get(user=self.kwargs.get('user'))
        qs = super().get_queryset()
        # 장고의 in은 튜플, 리스트, 쿼리셋 등 반복 가능한 객체를 조회한다. SQL문에서의 WHERE IN과 같은 역할을 한다.
        qs = qs.filter(user=user)
        return qs



# 업주 QNA에 접근하고 업주 유저인지 확인
class ShopQnaView(APIView):
    # 업주만 접근 가능하게 permissoin 설정
    # permission_classes = [IsShop]
    pass


