from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = "api-v1"

urlpatterns = [
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    
    path('change_password/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    
    path('profile/', views.ProfileApiView.as_view(), name='profile')
]
