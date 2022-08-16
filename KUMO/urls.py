from django.views.static import serve
from django.urls import re_path
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

from . import views

 
schema_view_v1 = get_schema_view(
    openapi.Info(
        title="KUMO API",
        default_version='v1',
        description="쿠폰을 모으다 API입니다.",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('customer/', include('customer.urls')),
    
    path('api-auth/', include('rest_framework.urls')),

    # API document generation with  drf_yasg
    url(r'^swagger(?P<format>\.json|\.yaml)/$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
]
