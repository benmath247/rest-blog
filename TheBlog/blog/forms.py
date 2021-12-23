from django import forms

from blog.models import Comment, Post


class PostCreateForm(forms.ModelForm):

    choices = [("coding", "coding"), ("life", "life"), ("nyc", "nyc")]

    class Meta:
        model = Post
        fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]
