from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.models import Coupon
from . import views


myprofile = views.MyProfileViewSet.as_view({
    'get' : 'list',
})

couponhistory = views.CouponHistoryViewSet.as_view({
    'get' : 'list',
})

mystamp =  views.StampView.as_view({
    'get' : 'list',
})

bookmark = views.BookmarkView.as_view({
    'get' : 'list',
})

near_shop = views.NearShopViewSet.as_view({
    'get' : 'list',
})

urlpatterns = [
    path('search/', views.SearchListView.as_view()),
    path('home/', views.HomeView.as_view(), name='view'),
    path('shop_detail/<str:user>/', views.ShopDetailView.as_view(), name='ShopDetailView'),
    path('profile/', myprofile),
    path('change_profile/', views.ChangeProfileView.as_view(), name="change_profile"),
    path('couponhistory/', couponhistory), 
    path('bookmark_add/<str:user>/', views.Bookmark_add),
    #path('bookmark/', views.BookmarkView.as_view()), # 북마크 리스트
    path('bookmark/', bookmark), # 북마크 리스트
    path('review_create/<str:user>/', views.ReviewCreateView.as_view(), name='cu_review'), # 가게 리뷰 생성, 수정하기
    path('review_list/<str:user>/', views.ReviewListView.as_view()), # 가게 리뷰 읽어오기
    path('review_putdel/<str:user>/<int:pk>/', views.ReviewUpdateDeleteView.as_view()), # 가게 리뷰 수정 및 삭제
    path('nearshop/', near_shop), # 1KM 이내 가게
    path('stamp/', mystamp), # 내 스탬프
    #path('qna/', views.CustomerQnaView.as_view()),
]