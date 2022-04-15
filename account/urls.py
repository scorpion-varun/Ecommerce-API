from django.urls import path
from account.views import UserRegistrationView, UserLoginView,UserProfileView,  LogoutView,LogoutAllView
from account.views import UserChangePasswordView
from account.views import SendPasswordResetemailView
from account.views import UserPasswordResetView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login-refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetemailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),


]
