from django import forms

from blog.models import Comment, Post, PostReaction


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]

class PostReactionForm(forms.ModelForm):
    class Meta:
        model = PostReaction
        fields = ["reaction"]
