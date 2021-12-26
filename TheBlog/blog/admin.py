from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from .models import Comment, Like, Post, PostReaction


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_on")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post")
    list_filter = ("user", "post")

admin.site.register(Like, LikeAdmin)


class PostReactionAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "reaction")

admin.site.register(PostReaction, PostReactionAdmin)




class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name")


admin.site.register(Comment, CommentAdmin)
