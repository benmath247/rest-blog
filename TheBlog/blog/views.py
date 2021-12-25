from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from blog.forms import CommentForm, PostCreateForm
from blog.models import Comment, CommentLike, Like, Post
from blog.serializers import (CommentLikeSerializer, CommentSerializer,
                              LikeSerializer, PostSerializer)


#### POST MODEL CRUD ###
def post_list(request):

    # sort by date created
    queryset = Post.objects.order_by("-created_on")
    return render(request, "index.html", context={"post_list": queryset})


def post_detail(request, slug):
    # slug is used to define which Post object will display
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    return render(
        request,
        "post_detail.html",
        context={"post": post, "comment_form": comment_form},
    )


def post_create(request):
    if request.method == "GET":
        # take form from post forms.py and put it into context for post_create.html
        form = PostCreateForm()
        return render(request, "post_create.html", context={"post_form": form})

    if request.method == "POST":
        # take fields from form and post them to db
        title = request.POST.get("title")
        content = request.POST.get("content")
        # Create a new Post object
        Post.objects.create(
            author=request.user,
            title=title,
            content=content,
        )
        return redirect("home")


def post_delete(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, slug=pk)
        post.delete()
        return redirect("home")


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "GET":
        form = PostCreateForm(initial={"title": post.title, "content": post.content})

        return render(
            request, "post_edit.html", context={"post_form": form, "post": post}
        )

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.status = request.POST.get("status")
        post.save()
        comment_form = CommentForm()
        return render(
            request,
            "post_detail.html",
            context={"post": post, "comment_form": comment_form},
        )


#### COMMENT MODEL CRUD ####


def add_comment(request, pk):
    if request.method == "GET":
        form = CommentForm()
        return render(request, "add_comment.html", context={"post_form": form})

    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        Comment.objects.create(post_id=pk, name=name, comment=comment)
        return redirect("home")


def comment_delete(request, pk):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return redirect("home")


#### LIKE MODEL CRUD ####
def like_view(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, id=request.POST.get("post_id"))
        if not Like.objects.filter(post=post, user=request.user):
            Like.objects.create(post=post, user=request.user)

        return redirect("post_detail", slug=post.slug)


def unlike_view(request, pk):
    if request.method == "POST":
        like = get_object_or_404(Like, pk=pk)
        like.delete()
        return redirect("home")


#### COMMENT LIKE MODEL CRUD ###
def like_a_comment_view(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, id=request.POST.get("post_id"))
        comment = Comment.objects.get(id=pk)
        if not CommentLike.objects.filter(
            comment_id=pk,
            user=request.user,
        ):
            CommentLike.objects.create(comment=comment, user=request.user)
        return redirect("post_detail", slug=post.slug)


def delete_comment_like(request, pk):
    if request.method == "POST":
        commentlike = get_object_or_404(CommentLike, pk=pk)
        commentlike.delete()
        return redirect("home")
