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



urlpatterns = [
    path('<int:pk>/', views.RootView.as_view()),
    path('search/', views.SearchListView.as_view()),
    re_path(r'^purchases/(?P<user>.+)/$', views.SearchListView.as_view()),
    path('<int:pk>/home/', views.HomeView.as_view(), name='view'),
    path('<int:pk>/profile/', myprofile),
    path('change_profile/<str:user>', views.ChangeProfileView.as_view(), name="change_profile"),
    #path('bookmark/', views.BookmarkView.as_view()),
    #path('neighborhood/', views.NeighborhoodView.as_view()),
    path('shopdetail/', shopdetail),
    path('<int:pk>/review/', user_review),
    path('stamp/', views.StampView.as_view(), name='mystamp'),
    path('qna/', views.CustomerQnaView.as_view()),
]