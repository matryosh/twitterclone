from django.urls import path

from .views import CreateUserView, UserHomePage

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name="signup"),
    path('<slug:username>/', UserHomePage.as_view(), name="userpage"),
]