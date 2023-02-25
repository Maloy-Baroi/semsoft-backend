from django.urls import path
from .views import RegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'App_login'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

