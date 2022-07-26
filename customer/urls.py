from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:pk>/', views.RootView.as_view()),
    path('search/', views.SearchView.as_view()),
    path('<int:pk>/profile/', views.ProfileView.as_view()),
    path('<int:pk>/bookmark/', views.BookmarkView.as_view()),
    path('neighborhood/', views.NeighborhoodView.as_view()),
    path('<int:pk>/stamp/', views.StampView.as_view()),
    path('qna/', views.CustomerQnaView.as_view()),
]