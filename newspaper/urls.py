from django.urls import path
from django.contrib.auth.views import LogoutView

from newspaper.views import (
    login_view,
    register_user,
    index,
)

urlpatterns = [
    path("", index, name="index"),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

app_name = "newspaper"
