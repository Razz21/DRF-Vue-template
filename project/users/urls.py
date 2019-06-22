from django.urls import path, include, re_path
from rest_auth.views import PasswordResetConfirmView
from knox.views import LogoutView
from rest_framework.routers import DefaultRouter
from .views import (
    UserAPI, 
    LoginView, 
    RegisterView, 
    TokenSessionLogoutView,
    UserViewSet,
    ValidateUsername,
)

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    # path("logout/", LogoutView.as_view()),
    path("logout/", TokenSessionLogoutView.as_view()),
    path("user/validate_username/", ValidateUsername.as_view()),
    path("user/", UserAPI.as_view()),
    re_path(
        r"^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("", include("rest_auth.urls")),
    path("", include("knox.urls")),
]
