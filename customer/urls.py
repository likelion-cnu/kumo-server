from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('mystamp', views.StampViewSet, basename='mystamp') 

detail_router = DefaultRouter()
detail_router.register('shopdetail', views.ShopDetailViewSet, basename='shopdetail') 

customer_profile = views.MyProfileViewSet.as_view({
    'get' : 'list',
})

bookmark = views.BookmarkView.as_view({
    'get' : 'list',
})



urlpatterns = [
    path('<int:pk>/', views.RootView.as_view()),
    path('<int:pk>/', views.HomeView.as_view()),
    path('search/', views.SearchListView.as_view()),
    re_path(r'^purchases/(?P<user>.+)/$', views.SearchListView.as_view()),
    path('<int:pk>/profile/', customer_profile),
    path("change_profile/<str:user>", views.ChangeProfileView.as_view(), name="change_profile"),

    path("", include(router.urls)),
#    path('<int:pk>/stamp/', views.StampView.as_view()),
    path("", include(detail_router.urls)),
#    path('')
#    path('neighborhood/', views.NeighborhoodView.as_view())
        
#    path('<int:pk>/bookmark/', bookmark),

    path('qna/', views.CustomerQnaView.as_view()),
]