from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from knox.models import AuthToken
from ..serializers import UserSerializer, KnoxSerializer
import pytest

pytestmark = pytest.mark.django_db


class TestUserSerializer(APITestCase):
    USERNAME = "test"
    PASS = "password"

    def setUp(self):
        self.user = self.setup_user()
        self.serializer = UserSerializer(instance=self.user)

    def setup_user(self):
        User = get_user_model()
        credentials = {"username": self.USERNAME, "password": self.PASS}
        return User.objects.create_user(**credentials)

    def test_contain_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(set(data.keys()), set(["id", "username", "email"]))

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.user.id)
        self.assertEqual(data["username"], self.USERNAME)
        self.assertEqual(data["email"], self.user.email)


class TestKnoxSerializer(APITestCase):
    USERNAME = "test"
    PASS = "password"

    def setUp(self):
        self.user = self.setup_user()
        self.token = AuthToken.objects.create(user=self.user)
        self.data = {"token": self.token[1], "user": self.user}
        self.serializer = KnoxSerializer(self.data)

    def setup_user(self):
        User = get_user_model()
        credentials = {"username": self.USERNAME, "password": self.PASS}
        return User.objects.create_user(**credentials)

    def test_contain_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(set(data.keys()), set(["token", "user"]))

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["token"], self.token[1])
        self.assertCountEqual(
            set(data["user"].keys()), set(["id", "username", "email"])
        )
        self.assertEqual(data["user"]["username"], self.USERNAME)
        self.assertEqual(data["user"]["id"], self.user.id)
        self.assertEqual(data["user"]["email"], self.user.email)

