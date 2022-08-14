from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path

from shop.models import Coupon
from . import views



myprofile = views.MyProfileViewSet.as_view({
    'get' : 'list',
})

shopdetail = views.ShopDetailViewSet.as_view({ 
    'get' : 'list',
})

user_review = views.ShopDetailViewSet.as_view({ 
    'post' : 'create',
})



shop_profile = views.BookmarkView.as_view({
    'get' : 'list',
})

urlpatterns = [
    path('search/', views.SearchListView.as_view()),
    re_path(r'^purchases/(?P<user>.+)/$', views.SearchListView.as_view()),
    path('home/', views.HomeView.as_view(), name='view'),
    path('profile/', myprofile),
    path('change_profile/', views.ChangeProfileView.as_view(), name="change_profile"),
    
    path('bookmark_add/', views.Bookmark_add),
    path('bookmark_remove/', views.Bookmark_remove),

    path('bookmark/', shop_profile),
    #path('neighborhood/', views.NeighborhoodView.as_view()),
    path('shopdetail/', shopdetail),
    path('review/', user_review),
    path('stamp/', views.StampView.as_view(), name='mystamp'),
    path('qna/', views.CustomerQnaView.as_view()),
]