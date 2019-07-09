from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from knox.models import AuthToken
from .. import views


class TestLoginView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.uri = "/api/auth/login/"
        self.view = views.LoginView.as_view()
        self.credentials = {"username": "test", "password": "testpassword"}

    def test_login(self):
        user = get_user_model().objects.create_user(**self.credentials)
        response = self.client.post(self.uri, self.credentials, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual("token" in response.data, True)

    def test_fail_wrong_credentials_login(self):
        wrong_credentials = {"username": "wrong", "password": "wrong_pass"}
        response = self.client.post(self.uri, wrong_credentials, follow=True)

        self.assertEqual(response.status_code, 400)

    def test_fail_empty_data_login(self):
        response = self.client.post(self.uri, {}, follow=True)
        self.assertEqual(response.status_code, 400)


class TestRegisterView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.uri = "/api/auth/register/"

        self.credentials = {
            "username": "test",
            "password1": "testpassword",
            "password2": "testpassword",
            "email": "mail@test.com",
        }

    def test_register(self):
        self.assertEqual(AuthToken.objects.count(), 0)
        response = self.client.post(self.uri, self.credentials, follow=True)

        self.assertEqual(response.status_code, 201)
        self.assertEqual("token" in response.data, True)
        self.assertEqual("user" in response.data, True)
        self.assertEqual(AuthToken.objects.count(), 1)

    def test_register_fail_wrong_data(self):
        self.assertEqual(AuthToken.objects.count(), 0)
        self.credentials["password2"] = "wrong"
        response = self.client.post(self.uri, self.credentials, follow=True)

        self.assertEqual(response.status_code, 400)
        self.assertEqual("token" in response.data, False)
        self.assertEqual("user" in response.data, False)
        self.assertEqual(AuthToken.objects.count(), 0)

    def test_register_fail_empty_data(self):
        self.assertEqual(AuthToken.objects.count(), 0)

        response = self.client.post(self.uri, {}, follow=True)
        self.assertEqual(response.status_code, 400)
        self.assertEqual("token" in response.data, False)
        self.assertEqual("user" in response.data, False)
        self.assertEqual(AuthToken.objects.count(), 0)


class TestUserAPIView(APITestCase):
    USERNAME = "test"
    PASS = "password"

    def setUp(self):
        self.factory = APIRequestFactory()
        self.uri = "/api/auth/user/"
        self.user = self.setup_user()
        self.token = AuthToken.objects.create(user=self.user)

    def setup_user(self):
        User = get_user_model()
        credentials = {"username": self.USERNAME, "password": self.PASS}
        return User.objects.create_user(**credentials)

    def test_get_method(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token[1])
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual('username' in response.data, True)
        self.assertEqual(response.data["id"], self.user.id)
        self.assertEqual(response.data["username"], self.USERNAME)
        self.assertEqual(response.data["email"], "")

    def test__fail_get_method_bad_auth_data(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + "invalid_token")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 401)

    def test__fail_get_method_no_data(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 401)


class TestLogoutView(APITestCase):
    USERNAME = "test"
    PASS = "password"

    def setUp(self):
        self.uri = "/api/auth/logout/"
        self.user = self.setup_user()
        self.token = AuthToken.objects.create(user=self.user)

    def setup_user(self):
        User = get_user_model()
        credentials = {"username": self.USERNAME, "password": self.PASS}
        return User.objects.create_user(**credentials)

    def test_logout(self):
        self.assertEqual(AuthToken.objects.count(), 1)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token[1])
        response = self.client.post(self.uri)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)
        self.assertEqual(AuthToken.objects.count(), 0)

        # token should be invalid after logout
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token[1])
        response = self.client.get("/api/auth/user/")
        self.assertEqual(response.status_code, 401)

    def test_fail_logout_bad_data(self):
        self.assertEqual(AuthToken.objects.count(), 1)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + "invalid_token")
        response = self.client.post(self.uri)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(AuthToken.objects.count(), 1)


class TestValidateUsernameView(APITestCase):
    USERNAME = "test"
    PASS = "password"

    def setUp(self):
        self.uri = "/api/auth/user/validate_username/"
        self.user = self.setup_user()

    def setup_user(self):
        User = get_user_model()
        credentials = {"username": self.USERNAME, "password": self.PASS}
        return User.objects.create_user(**credentials)

    def test_valid_username(self):
        response = self.client.post(self.uri, {"username": "valid"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["is_taken"], False)
        self.assertEqual("message" in response.data, False)

    def test_fail_username_taken(self):
        response = self.client.post(self.uri, {"username": self.USERNAME})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["is_taken"], True)
        self.assertEqual("message" in response.data, True)
