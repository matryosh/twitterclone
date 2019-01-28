from django.urls import path

from .views import CreateTweet

app_name = "Tweets"

urlpatterns = [
    path('', CreateTweet.as_view(), name='tweet'),
]