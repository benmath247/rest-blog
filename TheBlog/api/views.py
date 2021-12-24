from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Posts": {
            "list": "posts/",
            "details": "<slug>/",
            "edit": "<slug>/edit/",
            "delete": "<slug>/delete/",
            "create": "post/create/",
        },
        "Likes": {
            "List": "<slug>/likes/",
            "Add like": "<slug>/like/",
            "Remove like": "<slug>/unlike/",
        },
        "Comments": {
            "List": "<slug>/comments/",
            "Add comment": "<slug>/comment/add/",
            "Remove comment": "<slug>/<index>/comment/delete",
        },
        "CommentLikes": {
            "List": "<slug>/comment/likes",
            "Add comment like": "<slug>/comment/<index>/like/",
            "Remove comment like": "<slug>/comment/<index>/delete",
        },
        "Users": {"List": "users/", "details": "users/<username>"},
    }
    return Response(api_urls)
