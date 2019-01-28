from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.


class TweetModelBase(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    likes = models.PositiveIntegerField(default=0)

    date = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class TweetModel(TweetModelBase):

    tweet = models.CharField(max_length=140, default='')

    def __str__(self):

        return self.user.email.split('@')[0] + ': ' + self.tweet[0:9]


class TweetPictureModel(TweetModelBase):

    tweet = models.CharField(max_length=70, default='')

    picture = models.ImageField(upload_to='media/', default='media/kitten.jpg')


class TweetVideoModel(TweetModelBase):
    pass