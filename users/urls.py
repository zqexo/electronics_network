from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.utils import TokenObtainCustom
from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainCustom.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
