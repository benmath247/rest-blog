from typing import List

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from blog.forms import CommentForm, PostCreateForm
from blog.models import Comment, CommentLike, Like, Post, PostReaction
from blog.serializers import (
    CommentLikeSerializer,
    CommentSerializer,
    LikeSerializer,
    PostCreateSerializer,
    PostSerializer,
    ReactionSerializer,
)

### PAGINATION
class ResultsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5


# RetrieveUpdateAPIView - get requests retrieves 1, put request updates 1
# look at mixins
### POST CRUD ###

# LIST/CREATE
class PostListAPIView(ListCreateAPIView):

    serializer_class = PostSerializer
    pagination_class = ResultsPagination
    queryset = Post.objects.all()

    def create(self, *args, **kwargs):
        serializer = PostCreateSerializer(
            data={
                "title": self.request.POST.get("title"),
                "content": self.request.POST.get("content"),
            }
        )
        if serializer.is_valid():
            data = serializer.data
            data["author"] = self.request.user
            Post.objects.create(**data)
            # Post.objects.create(title=data['title'], content=data['content'], author=data['author'])
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


# DESTROY
class PostDestroyAPIView(DestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


# RETRIEVE/UPDATE
class PostRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.method == "GET":
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)


### LIKE CRUD ###

# LIST/CREATE
class LikeListAPIView(ListCreateAPIView):
    serializer_class = LikeSerializer
    pagination_class = ResultsPagination

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
        return post.likes.all()


# DESTROY
class LikeDestroyAPIView(DestroyAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self, *args, **kwargs):
        return Like.objects.all()


# RETRIEVE/UPDATE
class LikeRetrieveAPIView(RetrieveAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


### COMMENT CRUD

# LIST/CREATE
class CommentListAPIView(ListCreateAPIView):
    pagination_class = ResultsPagination
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
        return post.comments.all()


# DESTROY
class CommentDestroyAPIView(DestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.all()


# RETRIEVE/UPDATE
class CommentRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.method == "GET":
            return Comment.objects.all()
        return Comment.objects.filter(user=self.request.user)


### COMMENT LIKE CRUD

# LIST/CREATE
class CommentLikeListAPIView(ListCreateAPIView):
    pagination_class = ResultsPagination
    serializer_class = CommentLikeSerializer

    def get_queryset(self, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get("pk"))
        return comment.likes.all()


# DESTROY
class CommentLikeDestroyAPIView(DestroyAPIView):
    serializer_class = CommentLikeSerializer

    def get_queryset(self, *args, **kwargs):
        return CommentLike.objects.all()


# RETRIEVE/UPDATE
class CommentLikeRetrieveAPIView(RetrieveAPIView):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()


### REACTION CRUD ###

# LIST/CREATE
class ReactionListAPIView(ListCreateAPIView):
    serializer_class = ReactionSerializer

    def get_queryset(self, *args, **kwargs):
        return PostReaction.objects.all()
