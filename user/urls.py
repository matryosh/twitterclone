from django.urls import path
from django.views.decorators.cache import cache_page

from .views import CreateUserView, UserHomePage, CustomLogin, UpdateUser, UpdateProfilePicture

app_name = 'users'

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name="signup"),
    path('login/', CustomLogin.as_view(), name="login"),
    path('<slug:username>/', UserHomePage.as_view(), name="userpage"),
    path('<slug:username>/update/', UpdateUser.as_view(), name="updateuserpage"),
    path('<int:pk>/updatepicture/', UpdateProfilePicture.as_view(), name='updateprofilepicture'),
]

#cache_page(60*15)