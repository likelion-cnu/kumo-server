from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from shop.models import Coupon, Review
from accounts.models import ShopUser, User, CustomerUser

from .serializers import MyStampSerializer, CouponHistorySerializer, BookmarkSerializer, ShopbriefSerializer, UserProfileSerializer, ReviewCreatSerializer, ReviewCreateSerializer, UserProfileEditSerializer, SearchSerializer, HomeSerializer, BookmarkSerializer, ShopDetailSerializer, NearShopSerializer
from shop.serializers import ReviewSerializer, ShopProfileUserSerializer, ShopUserSerializer, CouponeSerializer

from accounts.permissons import IsCustomer
# Create your views here.



# 홈 뷰
class HomeView(APIView):
    #permission_classes = [IsCustomer]
    
    def get(self, request):
        queryset = User.objects.filter(username = self.request.user.username)
        serializer = HomeSerializer(queryset, many=True)
        return Response(serializer.data)


# 검색 기능
class SearchListView(generics.ListAPIView):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    #permission_classes = [IsCustomer]

    filter_backends = [SearchFilter]
    search_fields = ['shop_name']
    ordering_fields = ['shop_name']
    ordering = ['shop_name']
        

# myprofile - 나의 정보
class MyProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = UserProfileSerializer
    #permission_classes = [IsCustomer]

    def get(self, request, *args, **kwargs):    
        queryset = CustomerUser.objects.filter(user=self.request.user.username)
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)


# 나의 정보 수정
class ChangeProfileView(generics.UpdateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserProfileEditSerializer
    #permission_classes = [IsCustomer]

    def get_queryset(self):
        user = CustomerUser.objects.filter(user=self.request.user.username)
        qs = super().get_queryset()
        # 장고의 in은 튜플, 리스트, 쿼리셋 등 반복 가능한 객체를 조회한다. SQL문에서의 WHERE IN과 같은 역할을 한다.
        qs = qs.filter(user__in=user)
        return qs


# myprofile - 쿠폰 히스토리
class CouponHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponHistorySerializer
    #permission_classes = [IsCustomer]

    def list(self, request, *args, **kwargs):
        queryset = Coupon.objects.filter(writer=self.request.user.username)
        serializer = CouponHistorySerializer(queryset, many=True)
        return Response(serializer.data)
        #(request, *args, **kwargs)


# 내 스탬프
class StampView(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = MyStampSerializer
 #   permission_classes = [IsCustomer]

    def list(self, request, *args, **kwargs):
        queryset = Coupon.objects.filter(writer=self.request.user.username)
        serializer = MyStampSerializer(queryset, many=True)
        return Response(serializer.data)


# 내 주변 가게 - shop datail
class ShopDetailView(generics.RetrieveAPIView):
    queryset = ShopUser.objects.all()
    serializer_class = ShopDetailSerializer
    #permission_classes = [IsCustomer]
    lookup_field = 'user'

    def get(self, request, *args, **kwargs):
        queryset = ShopUser.objects.get(user=self.kwargs.get('user'))
        serializer = ShopDetailSerializer(queryset)
        return Response(serializer.data)


# review 리스트
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreatSerializer
    lookup_field = 'user'


# review 생성
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        cu = CustomerUser.objects.get(user=self.request.user.username)
        # self.kwargs.get('user')은 url에 넘겨진 인자를 가져온다.
        shop = ShopUser.objects.get(user=self.kwargs.get('user'))
        serializer.save(writer=cu, shopname=shop)
        


# review 수정 및 삭제
class ReviewUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

    def perform_update(self, serializer):
        cu = CustomerUser.objects.get(user=self.request.user.username)
        # self.kwargs.get('user')은 url에 넘겨진 인자를 가져온다.
        shop = ShopUser.objects.get(user=self.kwargs.get('user'))
        serializer.save(writer=cu, shopname=shop)

    def get_queryset(self):
        review = Review.objects.get(pk=self.kwargs.get('pk'))
        # 장고의 in은 튜플, 리스트, 쿼리셋 등 반복 가능한 객체를 조회한다. SQL문에서의 WHERE IN과 같은 역할을 한다.
        return review    


# bookmark한 가게들 출력
class BookmarkView(ReadOnlyModelViewSet):
    queryset = ShopUser.objects.all()
    serializer_class = ShopDetailSerializer


    def list(self, request, *args, **kwargs):
        customer_user = get_object_or_404(CustomerUser, user=request.user.username)
        bookmark_list = customer_user.bookmark_set.all()

        book_result = []
        for i in range(len(bookmark_list)-1):
            book_result.append(bookmark_list[i])
            
        result = ShopUser.objects.filter(user__in=book_result)
        serializer = ShopbriefSerializer(result, many=True)

        coupon = Coupon.objects.filter(writer=self.request.user.username)
        cu_serializer = CouponeSerializer(coupon, many=True)
        
        return Response(serializer.data + cu_serializer.data)


@api_view(['POST'])
def Bookmark_add(request, user):
    if request.method == 'POST':
        # 고객 유저를 업주 유저의 bookmarked_set에 추가하고, 삭제
        shop_user = get_object_or_404(ShopUser, user=user)
        customer_user = get_object_or_404(CustomerUser, user=request.user)
        if customer_user in shop_user.bookmarked_set.all():
            shop_user.bookmarked_set.remove(customer_user)
            customer_user.bookmark_set.remove(shop_user)
        else:
            shop_user.bookmarked_set.add(customer_user)
            customer_user.bookmark_set.add(shop_user)
        return Response(status=201)


# 1KM 거리에 있는 가게들만 조회
class NearShopViewSet(ReadOnlyModelViewSet):
    queryset = ShopUser.objects.all()
    serializer_class = NearShopSerializer

    def filter_by_distance_manual(self, qs):
        """좌표 기준 반경 1km 쿼리"""
        # data = 고객의 좌표
        data = self.request.query_params
        if self.action == 'list':
            lat = data.get('lat')
            lng = data.get('lng')
            if lat and lng:
                lat = float(lat)
                lng = float(lng)
                min_lat = lat - 0.009
                max_lat = lat + 0.009
                min_lon = lng - 0.015
                max_lon = lng + 0.01

                # 최소, 최대 위경도를 1km씩 설정해서 쿼리
                qs = qs.filter(lat__gte=min_lat, lat__lte=max_lat,
                            lng__gte=min_lon, lng__lte=max_lon)
        return qs
