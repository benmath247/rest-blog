import requests
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render


from blog.forms import CommentForm, PostCreateForm, PostReactionForm
from blog.models import Comment, CommentLike, Like, Post, PostReaction


def bitcoin_price(request):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    usd = data["bpi"]["USD"]["rate"]
    gbp = data["bpi"]["GBP"]["rate"]
    eur = data["bpi"]["EUR"]["rate"]
    return render(
        request,
        "bitcoin_price.html",
        context={"usd_btc": usd, "gbp_btc": gbp, "eur_btc": eur},
    )


#### POST MODEL CRUD ###
def post_list(request):

    # sort by date created
    queryset = Post.objects.order_by("-created_on")
    return render(request, "index.html", context={"post_list": queryset})


def post_detail(request, slug):
    # slug is used to define which Post object will display
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    reaction_form = PostReactionForm()

    return render(
        request,
        "post_detail.html",
        context={
            "post": post,
            "comment_form": comment_form,
            "reaction_form": reaction_form,
        },
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
        image = request.FILES.get("image")
        # Create a new Post object
        Post.objects.create(
            author=request.user, title=title, content=content, image=image
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


#### POSTREACTION MODEL CRUD ####
def postreaction_view(request, pk):
    if request.method == "GET":
        form = PostReactionForm()
        return render(request, "post_reaction.html", context={"reaction_form": form})
    if request.method == "POST":
        reaction = request.POST.get("reaction")
        reaction = PostReaction.objects.create(
            post_id=pk, reaction=reaction, user=request.user
        )
        return redirect("post_detail", slug=reaction.post.slug)
    if request.method == "DELETE":
        reaction = get_object_or_404(PostReaction, pk=pk)
        post = get_object_or_404(Post, id=request.POST.get("reactions"))
        reaction.delete()
        return redirect("post_detail", slug=post.slug)
