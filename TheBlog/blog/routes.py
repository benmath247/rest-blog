from django.urls import path

from blog.api import (
    PostListAPIView, 
    CommentLikeListAPIView, 
    CommentListAPIView, 
    LikeListAPIView, 
    PostDestroyAPIView, 
    LikeDestroyAPIView,
    CommentDestroyAPIView,
    CommentLikeDestroyAPIView
    )

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list-api-view"), #tested
    path("posts/<int:pk>/delete/", PostDestroyAPIView.as_view(), name='post-destroy-api-view'), #tested
    
    path("posts/<slug:slug>/likes/", LikeListAPIView.as_view(), name = 'like-list-api-view'), #tested
    path("posts/likes/<int:pk>/destroy/", LikeDestroyAPIView.as_view(), name = 'like-destroy-api-view'), #tested
    
    path("posts/<slug:slug>/comments/", CommentListAPIView.as_view(), name="comment-list-api-view"), #tested
    path("posts/comments/<int:pk>/destroy/", CommentDestroyAPIView.as_view(), name='comment-destroy-api-view'),

    path("posts/commentlikes/<int:pk>/", CommentLikeListAPIView.as_view(), name='comment-like-list-api-view'), #tested
    path("posts/comments/commentlikes/<int:pk>/destroy/", CommentLikeDestroyAPIView.as_view(), name='comment-like-destroy-api-view'),
]
