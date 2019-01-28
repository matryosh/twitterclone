from django.urls import path

from .views import CreateUserView, UserHomePage, CustomLogin

app_name = 'users'

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name="signup"),
    path('login/', CustomLogin.as_view(), name="login"),
    path('<slug:username>/', UserHomePage.as_view(), name="userpage"),
]