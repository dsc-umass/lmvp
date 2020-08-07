from django.urls import path
from .views import RegisterView,VerifyEmail,LoginApiView,PasswordTokenCheckAPI,RequestPasswordResetEmail,SetNewPasswordAPIView
from rest_framework_simplejwt.views import (
     TokenRefreshView,
)


urlpatterns = [
    path('register/',RegisterView.as_view(), name="register"),
    path('login/',LoginApiView.as_view(), name="login"),
    path('email-verify/',VerifyEmail.as_view(), name="email-verify"),
    # This uses the JWT Package to enable users to generate access tokens when logged in by using their current refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('request-reset-email/',RequestPasswordResetEmail.as_view(), 
          name='request-reset-email'),
    path('password-reset-complete', 
          SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('password-reset/<uidb64>/<token>/',
          PasswordTokenCheckAPI.as_view(), name='password-reset-confirm') #This url coiolects the encoded user information and token sent to their email for resseting password
]
