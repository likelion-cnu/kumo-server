from django.urls import path, include
from django.conf.urls import url


from . import views


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),

]







# from rest_framework_simplejwt import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )


#     url(r'^login/$', LoginView.as_view(), name='login'),
#     url(r'^logout/$', LogoutView.as_view(), name='logout'),

#     url(r'^rest-auth/', include('rest_auth.urls')),
#     url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#     # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
