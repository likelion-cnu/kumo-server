from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('myshop', views.MyShopViewSet, basename='myshop') 

review_router = DefaultRouter()
review_router.register('myshop_review', views.MyShopReviewViewSet, basename='myshop_review') 

check_qrcode = views.Check_QRcodeViewSet.as_view({
    'post' : 'create',
})
check_detail_qrcode = views.Check_QRcodeViewSet.as_view({
    'put' : 'update',
})

shop_profile = views.ProfileViewSet.as_view({
    'get' : 'list',
})


urlpatterns = [
    path("<int:pk>/", views.RootView.as_view()),
    
    # QR 체크해주는 뷰 Check_QRcode-> POST, get_Check_QRcode-> PUT
    path("Check_QRcode/", check_qrcode),
    path("get_Check_QRcode/", check_detail_qrcode),
    
    
    # 내 가게 데이터
    path("<int:pk>/shopdata/", views.ShopdataView.as_view()),

    # 내 가게 
    path("", include(router.urls)),
    
    # 내 가게 리뷰
    path("", include(review_router.urls)),

    # 업주 프로필
    path("profile/", shop_profile),

    # 업주 QnA
    path("qna/", views.ShopQnaView.as_view()),
]