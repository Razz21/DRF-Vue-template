from rest_framework import generics, permissions
from rest_framework.response import Response

from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_auth.serializers import UserDetailsSerializer
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings

from .serializers import UserSerializer, KnoxSerializer
from .utils import create_knox_token


class LoginView(LoginView):
    def get_response(self):
        serializer_class = self.get_response_serializer()

        data = {"user": self.user, "token": self.token}
        serializer = serializer_class(instance=data, context={"request": self.request})

        return Response(serializer.data, status=200)


class RegisterView(RegisterView):
    def get_response_data(self, user):
        return KnoxSerializer({"user": user, "token": self.token}).data

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        self.token = create_knox_token(None, user, None)
        complete_signup(
            self.request._request, user, allauth_settings.EMAIL_VERIFICATION, None
        )
        return user


class UserAPI(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


from knox.views import LogoutView
from django.contrib.auth.signals import user_logged_out
from rest_framework import status
from django.contrib.auth import logout as django_logout
from django.conf import settings


class TokenSessionLogoutView(LogoutView):
    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(
            sender=request.user.__class__, request=request, user=request.user
        )
        if getattr(settings, "REST_SESSION_LOGIN", True):
            django_logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
