from django.urls import path

from blog.api import (CommentDestroyAPIView, CommentLikeDestroyAPIView,
                      CommentLikeListAPIView, CommentLikeRetrieveAPIView,
                      CommentListAPIView, CommentRetrieveAPIView,
                      LikeDestroyAPIView, LikeListAPIView, LikeRetrieveAPIView,
                      PostDestroyAPIView, PostListAPIView,
                      PostRetrieveUpdateAPIView)

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list-api-view"),
    path("posts/<int:pk>/delete/", PostDestroyAPIView.as_view(), name='post-destroy-api-view'), 
    path("posts/<int:pk>/", PostRetrieveUpdateAPIView.as_view(), name = 'post-retrieve-api-view'),

    path("posts/<slug:slug>/likes/", LikeListAPIView.as_view(), name = 'like-list-api-view'),
    path("posts/likes/<int:pk>/destroy/", LikeDestroyAPIView.as_view(), name = 'like-destroy-api-view'),
    path("posts/likes/<int:pk>/", LikeRetrieveAPIView.as_view(), name = 'like-retrieve-api-view'), #untested

    path("posts/<slug:slug>/comments/list", CommentListAPIView.as_view(), name="comment-list-api-view"),
    path("posts/comments/<int:pk>/destroy/", CommentDestroyAPIView.as_view(), name='comment-destroy-api-view'),
    path("posts/comments/<int:pk>/", CommentRetrieveAPIView.as_view(), name = "comment-retrieve-api-view"), #untested

    path("posts/commentlikes/<int:pk>/list/", CommentLikeListAPIView.as_view(), name='comment-like-list-api-view'),
    path("posts/comments/commentlikes/<int:pk>/destroy/", CommentLikeDestroyAPIView.as_view(), name='comment-like-destroy-api-view'),
    path("posts/comments/commentlikes/<int:pk>/", CommentLikeRetrieveAPIView.as_view(), name='comment-like-retrieve-api-view') #untested
]
