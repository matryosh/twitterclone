from django.urls import path

from .views import CreateTweet, DeleteTweet

app_name = "tweets"

urlpatterns = [
    path('', CreateTweet.as_view(), name='tweet'),
    path('<int:pk>/delete/', DeleteTweet.as_view(), name='deletetweet'),
]