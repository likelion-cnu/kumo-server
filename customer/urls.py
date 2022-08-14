from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path

from shop.models import Coupon
from . import views



myprofile = views.MyProfileViewSet.as_view({
    'get' : 'list',
})

<<<<<<< HEAD
couponhistory = views.CouponHistoryViewSet.as_view({
    'get' : 'list',
})


=======
>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113
shopdetail = views.ShopDetailViewSet.as_view({ 
    'get' : 'list',
})

<<<<<<< HEAD
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
=======
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
>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113
    path('qna/', views.CustomerQnaView.as_view()),
]