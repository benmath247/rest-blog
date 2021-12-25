from typing import List
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from blog.forms import CommentForm, PostCreateForm
from blog.models import Comment, CommentLike, Like, Post

from blog.serializers import (
    PostSerializer,
    CommentLikeSerializer,
    CommentSerializer,
    LikeSerializer,
    PostCreateSerializer,
)
# RetrieveUpdateAPIView - get requests retrieves 1, put request updates 1
# look at mixins 
### POST CRUD ###

# LIST/CREATE
class PostListAPIView(ListCreateAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


    def create(self, *args, **kwargs):
        serializer = PostCreateSerializer(data={
            "title": self.request.POST.get('title'), 
            "content": self.request.POST.get('content')
        })
        if serializer.is_valid():
            data = serializer.data
            data['author'] = self.request.user
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
        return Post.objects.filter(author = self.request.user)
    
### LIKE CRUD ###

# LIST/CREATE
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

# RETRIEVE/UPDATE
class LikeRetrieveAPIView(RetrieveAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


### COMMENT CRUD

# LIST/CREATE
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

# RETRIEVE/UPDATE
class CommentRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


### COMMENT LIKE CRUD

# LIST/CREATE
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

# RETRIEVE/UPDATE
class CommentLikeRetrieveAPIView(RetrieveAPIView):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()