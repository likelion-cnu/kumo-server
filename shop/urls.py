from django.urls import path, include
from . import views

urlpatterns = [
    path("<int:pk>/", views.RootView.as_view()),
    
    # QR 체크해주는 뷰
    path("checkqrcode/", views.CheckQrView.as_view()),
    
    # Payment 등록해주는 뷰
    path("payment/", views.PaymentView.as_view()),

    path("<int:pk>/profile/", views.ProfileView.as_view()),
    path("<int:pk>/myshop/", views.MyShopView.as_view()),
    path("<int:pk>/shopdata/", views.ShopdataView.as_view()),
    path("qna/", views.ShopQnaView.as_view()),
]