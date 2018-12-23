from django.test import TestCase

from .models import (TweetModelBase,
                     TweetModel,
                     TweetPictureModel,
                     TweetVideoModel)
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.


class TweetModelBaseTests(TestCase):

    def setUp(self):
        self.user = User(
            age=25,
            email="oceanman@gmail.com",
            username="spongebob",
            password="patrick"
        )

        self.basetweet = TweetModelBase(
            user=self.user,
            likes=4,
        )

    def tweetmodelbasetests(self):

        self.assertEqual(self.basetweet.user, self.user)
        self.assertNotEqual(self.basetweet.likes, 4)


class TweetModelTest(TestCase):

    def setUp(self):
        self.user = User(
            age=25,
            email="oceanman@gmail.com",
            username="spongebob",
            password="patrick"
        )

        self.tweet = TweetModel(
            user=self.user,
            like=4,
            tweet="Witch's brew had me on the first sip, man."
        )

        self.assertLessEqual(len(self.tweet), 140)


class TweetPictureModelTests(TestCase):

    def setUp(self):
        pass


class TweetVideoModelTests(TestCase):

    def setUp(self):
        pass
