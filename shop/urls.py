from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('myshop', views.MyShopViewSet) 


urlpatterns = [
    path("<int:pk>/", views.RootView.as_view()),
    
    # QR 체크해주는 뷰
    path("Check_QRcode/", views.Check_QRcodeView.as_view()),
    
    # Payment 등록해주는 뷰
    path("payment/", views.PaymentView.as_view()),

    path("<int:pk>/profile/", views.ProfileView.as_view()),
    
    
    path("", include(router.urls)),
    
    
    path("<int:pk>/shopdata/", views.ShopdataView.as_view()),
    path("qna/", views.ShopQnaView.as_view()),
]