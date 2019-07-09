from django.urls import resolve, reverse

import pytest
from .. import views

pytestmark = pytest.mark.django_db


class TestUrls:
    def test_users_list(self):
        path = reverse("auth:usermodel-list")
        assert path == "/api/auth/users/"
        assert resolve(path).func.cls == views.UserViewSet

    def test_users_detail(self):
        path = reverse("auth:usermodel-detail", args=[1])
        assert path == "/api/auth/users/1/"
        assert resolve(path).func.cls == views.UserViewSet

    def test_register(self):
        path = reverse("auth:register")
        assert path == "/api/auth/register/"
        assert resolve(path).func.cls == views.RegisterView

    def test_login(self):
        path = reverse("auth:login")
        assert path == "/api/auth/login/"
        assert resolve(path).func.cls == views.LoginView

    def test_login(self):
        path = reverse("auth:logout")
        assert path == "/api/auth/logout/"
        assert resolve(path).func.cls == views.TokenSessionLogoutView

    def test_validate_username(self):
        path = reverse("auth:validate_username")
        assert path == "/api/auth/user/validate_username/"
        assert resolve(path).func.cls == views.ValidateUsername
