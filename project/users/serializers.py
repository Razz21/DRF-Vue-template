from django.contrib.auth import authenticate, get_user_model
from django.conf import settings

from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class KnoxSerializer(serializers.Serializer):
    """
    Serializer for Knox authentication.
    """

    token = serializers.CharField()
    user = UserSerializer()
