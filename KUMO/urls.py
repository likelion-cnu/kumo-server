from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('customer/', include('customer.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
]
