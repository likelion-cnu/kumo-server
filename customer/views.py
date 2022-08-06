from csv import writer
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from shop.models import Coupon, Review
from accounts.models import ShopUser, User, CustomerUser

from .serializers import MyStampSerializer, CouponHistorySerializer, UserProfileSerializer, ReviewCreatSerializer, UserProfileEditSerializer, SearchSerializer
from shop.serializers import ReviewSerializer, ShopProfileUserSerializer, ShopUserSerializer

from accounts.permissons import IsCustomer
# Create your views here.


########## 루트 페이지에 로그인 되어있는지와 고객 유저인지 확인
class RootView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass   
        

# 가게를 검색하는 뷰
class SearchListView(generics.ListAPIView):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['shop_name']

    def get_queryset(self):
        queryset = ShopUser.objects.all()
        user = self.request.query_params.get('user')   
        if user.is_authenticated:
            queryset = queryset.filter(search__user=user)
            return queryset
        else: 
            return ShopUser.objects.none()


#QR보여주는 홈을 띄우는 뷰
class HomeView(APIView):
    def get(self, request, format=None):
        qrcode = request.user.auth_token.get()

 


################# 북마크한 리스트를 띄우는 뷰
#class BookmarkView(generics.ListCreateAPIView):
#    def get_queryset(self):
#        queryset = super().get_queryset()
#        return queryset.filter(bookmarked_set=self.request.user)

class BookmarkView(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.filter('bookmark_set') #북마크셋을 불러오기
    serializer_class = MyStampSerializer

    def get_queryset(self):
        queryset = CustomerUser.objects.filter('bookmark_set'==True).all() #blank=True가 true일때
        super().get_queryset()
        return queryset


# 고객 프로필을 띄우는 뷰
class MyProfileViewSet(viewsets.ViewSet):
    def list(self, request, pk):
        
        queryset = CustomerUser.objects.filter(user=self.request.user.username)
        serializer = UserProfileSerializer(queryset, many=True)

        queryset2 = Coupon.objects.filter(writer=self.request.user.username)
        serializer2 = CouponHistorySerializer(queryset2, many=True)

        return Response(serializer.data + serializer2.data)
    

# 고객 프로필 변경하는 뷰
class ChangeProfileView(generics.UpdateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserProfileEditSerializer

    lookup_field = 'user'


    def get_queryset(self):
        user = CustomerUser.objects.filter(user=self.request.user.username)
        qs = super().get_queryset()
        # 장고의 in은 튜플, 리스트, 쿼리셋 등 반복 가능한 객체를 조회한다. SQL문에서의 WHERE IN과 같은 역할을 한다.
        qs = qs.filter(user__in=user)
        return qs





# 가게 세부정보랑 리뷰를 띄우는 뷰
class ShopDetailViewSet(viewsets.ModelViewSet):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    

    def list(self, request, *args, **kwargs):

        queryset = CustomerUser.objects.filter(review_writer=self.request.user)
        serializer = UserProfileSerializer(queryset, many=True)
        
        review = Review.objects.filter(writer=self.request.user.username)
        rev_serializer = ReviewSerializer(review, many=True)
        
        return Response(serializer.data + rev_serializer.data)

    @action(detail=False, methods=['POST']) 
    def create_review(self, request):
        serializer = ReviewCreatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    

    def get_queryset(self):
        user = CustomerUser.objects.filter(user=self.request.user)
        qs = super().get_queryset()
        # 장고의 in은 튜플, 리스트, 쿼리셋 등 반복 가능한 객체를 조회한다. SQL문에서의 WHERE IN과 같은 역할을 한다.
        qs = qs.filter(user__in=user)
        return qs

################보류/ 근처 가게를 띄우는 뷰
class NeighborhoodView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass


# 고객의 스탬프 갯수를 띄우는 뷰
class StampViewSet(viewsets.ReadOnlyModelViewSet):
    # 고객만 접근 가능하게 permissoin 설정
    queryset = Coupon.objects.all()
    serializer_class = MyStampSerializer
    permission_classes = [IsCustomer]
    pass


# 고객의 QNA를 띄우는 뷰
class CustomerQnaView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass