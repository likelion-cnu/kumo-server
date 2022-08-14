from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path

from shop.models import Coupon
from . import views



myprofile = views.MyProfileViewSet.as_view({
    'get' : 'list',
})

couponhistory = views.CouponHistoryViewSet.as_view({
    'get' : 'list',
})


shopdetail = views.ShopDetailViewSet.as_view({ 
    'get' : 'list',
})

user_review = views.ReviewCreateViewSet.as_view({ 
    'get' : 'list',
})

post_review = views.ReviewCreateViewSet.as_view({ 
    'post' : 'create'
})

shop_profile = views.BookmarkView.as_view({
    'get' : 'list',
})

mystamp =  views.StampView.as_view({
    'get' : 'list',
})


urlpatterns = [
    path('search/', views.SearchListView.as_view()),
    re_path(r'^purchases/(?P<user>.+)/$', views.SearchListView.as_view()),
    path('home/', views.HomeView.as_view(), name='view'),
    path('profile/', myprofile),
    path('change_profile/', views.ChangeProfileView.as_view(), name="change_profile"),
    path('couponhistory/', couponhistory),
    path('bookmark_add/', views.Bookmark_add),
    path('bookmark_remove/', views.Bookmark_remove),
    path('review/', user_review),
    path('reviewer/', post_review),    
    #path('neighborhood/', views.NeighborhoodView.as_view()),
    path('shopdetail/', shopdetail),
    path('stamp/', mystamp),
    path('qna/', views.CustomerQnaView.as_view()),
]