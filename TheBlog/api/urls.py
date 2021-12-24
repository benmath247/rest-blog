from django.contrib import admin
from django.urls import path
from api.views import user_details
from api.views import like_list
from api.views import (
    # postlist,
    userlist,
    post_details,
    post_delete,
    comment_list,
    commentlikes_list,
    PostListAPIView,
    CommentListAPIView,
)

from api.views import apiOverview

urlpatterns = [
    path("", apiOverview),
    path("posts/", PostListAPIView.as_view(), name="post-list-api-view"),
    path("users/", userlist),
    path("<slug:slug>/", post_details),
    path("<slug:slug>/delete/", post_delete),
    path("<slug:slug>/likes/", like_list),
    path(
        "<slug:slug>/comments/",
        CommentListAPIView.as_view(),
        name="comment-list-api-view",
    ),
    path("users/<int:pk>/", user_details),
    path("<slug:slug>/comment/<int:pk>/likes", commentlikes_list),
]
