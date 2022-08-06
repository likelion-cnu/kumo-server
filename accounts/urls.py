from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.hashers import check_password


from . import views


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    
    path("change_pwd/<str:username>", views.ChangePwdView.as_view(), name="change_pwd")
]




