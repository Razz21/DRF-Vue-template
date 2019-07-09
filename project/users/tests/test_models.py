from rest_framework.test import APITestCase

import pytest
from django.conf import settings

pytestmark = pytest.mark.django_db

# class TestUserModel(APITestCase):
#     def setUp(self, User: settings.AUTH_USER_MODEL):
#         self.user = User.objects.create_user("test", "", "password")
