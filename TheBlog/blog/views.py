from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render


from blog.forms import CommentForm, PostCreateForm
from blog.models import Comment, CommentLike, Like, Post


def post_list(request):
    queryset = Post.objects.order_by("-created_on")
    return render(request, "index.html", context={"post_list": queryset})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    total_likes = "total_likes"
    comment_form = CommentForm()
    return render(
        request,
        "post_detail.html",
        context={"post": post, "comment_form": comment_form},
    )


def post_create(request):
    if request.method == "GET":
        form = PostCreateForm()
        return render(request, "post_create.html", context={"post_form": form})

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        instance = Post.objects.create(
            author=request.user,
            title=title,
            content=content,
        )
        return redirect("home")


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
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
        return redirect("home")


def add_comment(request, pk):
    if request.method == "GET":
        form = CommentForm()
        return render(request, "add_comment.html", context={"post_form": form})

    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        Comment.objects.create(post_id=pk, name=name, comment=comment)
        return redirect("home")


def like_view(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, id=request.POST.get("post_id"))
        if not Like.objects.filter(post=post, user=request.user):
            Like.objects.create(post=post, user=request.user)

        return redirect("post_detail", slug=post.slug)


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
