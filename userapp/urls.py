from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'userapp'

urlpatterns = [

    
	# Admin Site URLs

    # Client Site URLs
    path('', ClientHomeView.as_view(), name="clienthome"),


    # Api Urls
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('login/', LoginAPIView.as_view(), name="login"),

    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name="password-reset-confirm"),
    path('request-reset-email/', RequestPasswordResetView.as_view(), name="request-reset-email"),

    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name="password-reset-complete"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]