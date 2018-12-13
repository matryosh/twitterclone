from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()


class CreateUserTestCase(TestCase):

    def setUp(self):

        self.user = User(
            age=25,
            email="oceanman@gmail.com",
            username="spongebob",
            password="patrick"
        )

    def test_user(self):
        self.assertEqual(self.user.email, "oceanman@gmail.com", "These emails aren't equal")
        self.assertEqual(self.user.age, 25, "These ages aren't equal")
        self.assertEqual(self.user.username, "spongebob", "These usernames aren't equal")
        self.assertEqual(self.user.password, "patrick", "These passwords aren't equal")