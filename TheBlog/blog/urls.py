from django.urls import path

from blog import views

urlpatterns = [
    path("", views.post_list, name="home"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("post/<slug:slug>/delete/", views.post_delete, name="post_delete"),
    path("post/<slug:slug>/edit/", views.post_edit, name="post_edit"),
    path("like/<int:pk>", views.like_view, name="like_post"),
    path("postreaction/<int:pk>", views.postreaction_view, name="reaction_post"),
    path("post/<int:pk>/add-comment/", views.add_comment, name="add_comment"),
    path(
        "commentlike/<int:pk>/add-commentlike/",
        views.like_a_comment_view,
        name="like_comment",
    ),
    path("crypto/", views.bitcoin_price, name="crypto")
]
