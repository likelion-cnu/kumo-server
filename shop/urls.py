from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# 내 가게 url
router = DefaultRouter()
router.register('myshop', views.MyShopViewSet, basename='myshop') 

# 내 가게 데이터 url
data_router = DefaultRouter()
data_router.register('myshop_data', views.ShopdataView, basename='myshop_data') 


# # QR 생성시 
# check_qrcode = views.Check_QRcodeViewSet.as_view({
#     'post' : 'create',
# })

# # QR 업데이트 시
# check_detail_qrcode = views.Check_QRcodeViewSet.as_view({
#     'put' : 'update',
# })

# 업주 프로필 
shop_profile = views.ProfileViewSet.as_view({
    'get' : 'list',
})


urlpatterns = [
    path("", views.RootView.as_view()),
    

    # QR 체크해주는 뷰 Check_QRcode-> POST, get_Check_QRcode-> PUT
    path("qrcheck/<str:user>/", views.QRCheck),
    path("Coupon_add/<str:user>/", views.Coupon_add),
    

    # 내 가게 데이터
    path("", include(router.urls)),


    # 내 가게 
    path("", include(data_router.urls)),
    

    # 업주 프로필
    path("profile/", shop_profile),

    path("change_profile/<str:user>/", views.ChangeProfileView.as_view(), name="change_profile"),

    # 업주 QnA
    path("qna/", views.ShopQnaView.as_view()),
]