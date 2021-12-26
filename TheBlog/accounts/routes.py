from django.urls import path

from accounts.api import (UserDestroyAPIView, UserListAPIView,
                          UserRetrieveAPIView)

urlpatterns = [
    path("accounts/", UserListAPIView.as_view(), name="user-list-api-view"),
    path("accounts/<int:pk>/destroy", UserDestroyAPIView.as_view(), name="user-destroy-api-view"),
    path("accounts/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-retrieve-api-view")
]