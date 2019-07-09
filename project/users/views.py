from django.contrib.auth import get_user_model
from django.contrib.auth import logout as django_logout
from django.contrib.auth.signals import user_logged_out
from django.conf import settings

from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from knox.models import AuthToken
from knox.auth import TokenAuthentication
from knox.views import LogoutView

from rest_auth.serializers import UserDetailsSerializer
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings

from .serializers import UserSerializer, KnoxSerializer
from .utils import create_knox_token


User = get_user_model()


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
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class TokenSessionLogoutView(LogoutView):
    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(
            sender=request.user.__class__, request=request, user=request.user
        )
        if getattr(settings, "REST_SESSION_LOGIN", True):
            django_logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class ValidateUsername(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        data = {"is_taken": User.objects.filter(username__iexact=username).exists()}
        if data["is_taken"]:
            data[
                "message"
            ] = "Username has already been taken, please select another one."
        return Response(data)
