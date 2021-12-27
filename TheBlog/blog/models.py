from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify

from elasticsearch_dsl import Q as ESQ

from accounts.models import User


class PostQuerySet(models.QuerySet):
    def search(self, search_query):
        from blog.documents import PostDocument

        query = ESQ(
            "multi_match",
            query=search_query,
            type="cross_fields",
            fields=["title"],
        )

        # get post documents
        res = (
            PostDocument.search().query(query).execute()
        )
        post_ids = []
        for hit in res.hits:
            post_ids.append(hit.id)
        posts = self.filter(id__in=post_ids)
        return posts


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    objects = PostQuerySet.as_manager()

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

    @cached_property
    def total_likes_reactions(self):
        likes = self.post_reactions.filter(reaction="👍")
        return likes.count()

    @cached_property
    def total_loves_reactions(self):
        loves = self.post_reactions.filter(reaction="💖")
        return loves.count()

    @cached_property
    def total_sad_reactions(self):
        sads = self.post_reactions.filter(reaction="😭")
        return sads.count()

    @cached_property
    def total_angry_reactions(self):
        angrys = self.post_reactions.filter(reaction="😡")
        return angrys.count()

    @cached_property
    def total_fire_reactions(self):
        fires = self.post_reactions.filter(reaction="🔥")
        return fires.count()

    @cached_property
    def total_taco_reactions(self):
        tacos = self.post_reactions.filter(reaction="🌮")
        return tacos.count()

    @cached_property
    def total_reactions(self):
        reactions = self.post_reactions.all()
        return reactions.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=180, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="comments"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return "%s = %s" % (self.post.title, self.name)

    @cached_property
    def total_likes(self):
        return self.likes.count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_likes")
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-created_on"]


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_likes"
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-created_on"]


class PostReaction(models.Model):
    CHOICES = [
        ("👍", "👍"),
        ("💖", "💖"),
        ("😭", "😭"),
        ("😡", "😡"),
        ("🔥", "🔥"),
        ("🌮", "🌮"),
    ]
    reaction = models.CharField(max_length=10, choices=CHOICES, null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_reactions"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reactions"
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-created_on"]
