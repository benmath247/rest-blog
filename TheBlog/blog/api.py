from typing import List
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.forms import CommentForm, PostCreateForm
from blog.models import Comment, CommentLike, Like, Post

from blog.serializers import (
    PostSerializer,
    CommentLikeSerializer,
    CommentSerializer,
    LikeSerializer,
)

### POST CRUD ###

# LIST
class PostListAPIView(ListCreateAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


# DESTROY
class PostDestroyAPIView(DestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


### LIKE CRUD ###

# LIST
class LikeListAPIView(ListCreateAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
        return post.likes.all()

# DESTROY
class LikeDestroyAPIView(DestroyAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self, *args, **kwargs):
        return Like.objects.all()


### COMMENT CRUD

# LIST
class CommentListAPIView(ListCreateAPIView):

    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
        return post.comments.all()

#DESTROY
class CommentDestroyAPIView(DestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.all()


### COMMENT LIKE CRUD

# LIST
class CommentLikeListAPIView(ListCreateAPIView):

    serializer_class = CommentLikeSerializer

    def get_queryset(self, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get("pk"))
        return comment.likes.all()

# DESTROY
class CommentLikeDestroyAPIView(DestroyAPIView):
    serializer_class = CommentLikeSerializer

    def get_queryset(self, *args, **kwargs):
        return CommentLike.objects.all()
