from django.shortcuts import render
from blog.models import CommentLike

from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    CommentLikeSerializer,
    CommentSerializer,
    PostSerializer,
    UserSerializer,
    LikeSerializer,
)

from blog.models import Post, Like, Comment
from accounts.models import User

from django.shortcuts import get_object_or_404

# Create your views here.

# instructions on how to user the api
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Posts": {
            "list": "posts/",  # done
            "details": "<slug>/",  # done
            "edit": "<slug>/edit/",
            "delete": "<slug>/delete/",  # done
            "create": "post/create/",
        },
        "Likes": {
            "List": "<slug>/likes/",  # done
            "Add like": "<slug>/like/",
            "Remove like": "<slug>/unlike/",
        },
        "Comments": {
            "List": "<slug>/comments/",  # done
            "Add comment": "<slug>/comment/add/",
            "Remove comment": "<slug>/<index>/comment/delete",
        },
        "CommentLikes": {
            "List": "<slug>/comment/<index>/likes",
            "Add comment like": "<slug>/comment/<index>/like/",
            "Remove comment like": "<slug>/comment/<index>/delete",
        },
        "Users": {"List": "users/", "details": "users/<username>"},  # done  # done
    }
    return Response(api_urls)


"""
@api_view(["GET"])
def postlist(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
"""


# class PostListAPIView(ListCreateAPIView):

#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class CommentListAPIView(ListCreateAPIView):

#     serializer_class = CommentSerializer

#     def get_queryset(self, *args, **kwargs):
#         post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
#         return post.comments.all()


@api_view(["GET"])
def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def post_delete(request, pk):
    post = get_object_or_404(Post, slug=pk)
    post.delete()
    return Response("deleted post")


@api_view(["GET"])
def like_list(request, slug):
    post = get_object_or_404(Post, slug=slug)
    likes = Like.objects.all().filter(post=post)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def comment_list(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.all().filter(post=post)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def commentlikes_list(request, pk, slug):
    post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.get(id=pk)
    likes = CommentLike.objects.all().filter(comment=comment)
    serializer = CommentLikeSerializer(likes, post, many=True)
    if serializer.is_valid():
        return Response(serializer.data)


# @api_view(["GET"])
# def userlist(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)


# @api_view(["GET"])
# def user_details(request, pk):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)

