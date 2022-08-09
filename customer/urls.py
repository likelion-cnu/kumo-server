from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('myprofile', views.MyProfileViewSet, basename='myprofile') 


urlpatterns = [
    path('<int:pk>/', views.RootView.as_view()),
]