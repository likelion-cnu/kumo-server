from csv import writer
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
<<<<<<< HEAD
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
=======
>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113

from shop.models import Coupon, Review
from accounts.models import ShopUser, User, CustomerUser

<<<<<<< HEAD
from .serializers import MyStampSerializer, CouponHistorySerializer, UserProfileSerializer, ReviewCreatSerializer, UserProfileEditSerializer, SearchSerializer, HomeSerializer, BookmarkSerializer, ShopDetailSerializer
from shop.serializers import ReviewSerializer, ShopProfileUserSerializer, ShopUserSerializer, CouponeSerializer
=======
from .serializers import MyStampSerializer, CouponHistorySerializer, UserProfileSerializer, ReviewCreatSerializer, UserProfileEditSerializer, SearchSerializer, HomeSerializer
from shop.serializers import ReviewSerializer, ShopProfileUserSerializer, ShopUserSerializer
>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113

from accounts.permissons import IsCustomer
# Create your views here.


########## 루트 페이지에 로그인 되어있는지와 고객 유저인지 확인
class RootView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass 

class HomeView(APIView):
<<<<<<< HEAD

    lookup_field = 'username'
    
    def get(self, request):
        queryset = User.objects.filter(username = self.request.user.username)
        serializer = HomeSerializer(queryset, many=True)
        return Response(serializer.data)


=======
    def get(self, request):
        pk = request.GET.get('pk')
        queryset = User.objects.get(category = pk)
        serializer = HomeSerializer(queryset, many=True)
        return Response(serializer.data)

>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113
class SearchListView(generics.ListAPIView):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['shop_name']

    def get_queryset(self):
        queryset = ShopUser.objects.all()
        user = self.request.query_params.get('user')   
        if user is not None and user.is_axtive :
            queryset = queryset.objects.filter(user=self.request.user)
            return queryset
        else: 
            return ShopUser.objects.none()
<<<<<<< HEAD



# myprofile - 나의 정보
class MyProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):    
        queryset = CustomerUser.objects.filter(user=self.request.user)
        serializer = UserProfileSerializer(queryset, many=True)
        return super().get(serializer.data)


#나의 정보 수정
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


# myprofile - 쿠폰 히스토리
class CouponHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponHistorySerializer

    def list(self, request, *args, **kwargs):
        #permission_classes = [IsCustomer]
        queryset = Coupon.objects.filter(writer=self.request.user.username)
        serializer = CouponHistorySerializer(queryset, many=True)
        return super().list(serializer.data)
        #(request, *args, **kwargs)


# 내 스탬프
class StampView(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = MyStampSerializer
 #   permission_classes = [IsCustomer]

    def list(self, request, *args, **kwargs):
        queryset = Coupon.objects.filter(writer=self.request.user.username)
        serializer = MyStampSerializer(queryset, many=True)
        return super().list(serializer.data)




# 내 주변 가게 - shop datail
class ShopDetailViewSet(viewsets.ReadOnlyModelViewSet):
    # 업주만 접근 가능하게 permissoin 설정
    queryset = ShopUser.objects.all()
    serializer_class = ShopDetailSerializer
 #   permission_classes = [IsCustomer]

    def list(self, request, *args, **kwargs):    
        queryset = ShopUser.objects.filter(user=self.request.user.username)
        serializer = ShopDetailSerializer(queryset, many=True)
        return super().list(serializer.data)
        

# shop detail 하단 - review list        
class ReviewListViewSet(viewsets.ReadOnlyModelViewSet):
    #queryset = Review.objects.all()
    #serializer_class= ReviewSerializer

    
    def list(self, request):
        queryset = Review.objects.filter(writer=self.request.user.username)
        serializer = ReviewSerializer(queryset, many=True)

        return Response(serializer.data)


#review 생성
class ReviewCreateViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class= ReviewSerializer

    def list(self, request, *args, **kwargs):    
        queryset = Review.objects.filter(user=self.request.user.username)
        serializer = ReviewCreatSerializer(queryset, many=True)
        return Response(self, request, *args, **kwargs)
=======



# 고객 프로필을 띄우는 뷰
class MyProfileViewSet(viewsets.ViewSet):
    def list(self, request, pk):
        
        queryset = CustomerUser.objects.filter(user=self.request.user.username)
        serializer = UserProfileSerializer(queryset, many=True)

        queryset2 = Coupon.objects.filter(writer=self.request.user.username)
        serializer2 = CouponHistorySerializer(queryset2, many=True)

        return Response(serializer.data + serializer2.data)

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


class StampView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = MyStampSerializer
    permission_classes = [IsCustomer]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = MyStampSerializer(queryset, many=True)
        return Response(serializer.data)

class ShopDetailViewSet(viewsets.ModelViewSet):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    

    def list(self, request, *args, **kwargs):

        queryset = CustomerUser.objects.filter(review_writer=self.request.user)
        serializer = UserProfileSerializer(queryset, many=True)
        
        review = Review.objects.filter(writer=self.request.user.username)
        rev_serializer = ReviewSerializer(review, many=True)
        
        return Response(serializer.data + rev_serializer.data)
>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113

    @action(detail=False, methods=['POST']) 
    def create(self, request):
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
<<<<<<< HEAD

        

# bookmark한 가게들 출력
class BookmarkView(ReadOnlyModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = BookmarkSerializer
    #permission_classes = [IsCustomer]

    def list(self, request, *args, **kwargs):
        queryset = CustomerUser.objects.filter(user=self.request.user.username)
        serializer = BookmarkSerializer(queryset, many=True)
        
        coupon = Coupon.objects.filter(writer=self.request.user.username)
        cu_serializer = CouponeSerializer(coupon, many=True)
        
        return Response(self,request, *args, **kwargs)


@api_view(['POST'])
def Bookmark_add(request):
    if request.method == 'POST':
        bookmarked_user = ShopUser.objects.filter(user=request.user.username)
        request.user.bookmark_set.add(bookmarked_user)
        bookmarked_user.add(request.user)

    return Response(status=201)

@api_view(['POST'])
def Bookmark_remove(request):
    if request.method == 'POST':
        bookmarked_user = ShopUser.objects.filter(user=request.user.username)
        request.user.bookmark_set.remove(bookmarked_user)
        bookmarked_user.remove(request.user)
    return Response(status=201)




=======


#class BookmarkView(generics.ListCreateAPIView):
#    queryset = CustomerUser.objects.filter('bookmark_set') #북마크셋을 불러오기
#    serializer_class = MyStampSerializer
>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113

#    def get_queryset(self):
#        queryset = CustomerUser.objects.filter('bookmark_set'==True).all() #blank=True가 true일때
#        super().get_queryset()
#        return queryset
#ValueError: too many values to unpack (expected 2)

# 고객의 QNA를 띄우는 뷰
class CustomerQnaView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass