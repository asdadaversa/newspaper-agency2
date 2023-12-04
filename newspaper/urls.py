from django.urls import path
from django.contrib.auth.views import LogoutView

from newspaper.views import (
    login_view,
    register_user,
    index,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"
    ),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),

    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),

    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete"
    ),

]

app_name = "newspaper"
