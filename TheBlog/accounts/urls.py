from django.urls import path

from accounts import views

urlpatterns = [
    path("create/", views.create_account, name="create_account"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("api/<int:pk>/", views.user_details, name="user_details"),
    path("api/users/all", views.userlist, name="list_users")
]
