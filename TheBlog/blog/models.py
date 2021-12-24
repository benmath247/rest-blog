from django.db import models
from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify
from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    @cached_property
    def total_likes(self):
        return self.likes.count()

    @cached_property
    def total_comments(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=180, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s = %s" % (self.post.title, self.name)

    @cached_property
    def total_likes(self):
        return self.likes.count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_likes")


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_likes"
    )
