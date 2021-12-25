
from django.test import TestCase
from django.shortcuts import reverse
from blog.models import Comment, CommentLike, Post, Like
from accounts.models import User
from rest_framework.test import APITestCase

# Create your tests here.


class PostListTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email="example@gmail.com")

        self.post_1 = Post.objects.create(
            author=user, content="my content1", title="my title1"
        )
        self.post_2 = Post.objects.create(
            author=user, content="my content2", title="my title2"
        )
        self.post_3 = Post.objects.create(
            author=user, content="my content3", title="my title3"
        )
        self.user=user

    @property
    def url(self):
        return reverse("post-list-api-view")

    def test_get(self):
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()[0]["title"], self.post_3.title)
        self.assertEqual(res.json()[1]["title"], self.post_2.title)
        self.assertEqual(res.json()[2]["title"], self.post_1.title)

    def test_post(self):
        self.client.force_login(self.user)
        data = {"title": "title", "content": "content"}
        res = self.client.post(self.url, data=data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(len(Post.objects.all()), 4)

class PostDestroyTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email="example@gmail.com")
        self.post_1 = Post.objects.create(
            author=user, content="my content1", title="my title1"
        )

    @property
    def url(self):
        return reverse("post-destroy-api-view", kwargs={"pk": self.post_1.pk})

    def test_delete(self):
        res = self.client.delete(self.url)
        self.assertEqual(res.status_code, 204)
        self.assertEqual(len(Post.objects.all()), 0)

class CommentListTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email="example@gmail.com")

        self.post_1 = Post.objects.create(
            author=user, content="my content1", title="my title1"
        )

        for i in range(10):
            post_comment = Comment.objects.create(
                post=self.post_1, name="my name", comment="my comment"
            )

    @property
    def url(self):
        return reverse("comment-list-api-view", kwargs={"slug": self.post_1.slug})

    def test_get(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 10)

    def test_post(self):
        self.user= User.objects.get(email="example@gmail.com")
        self.client.force_login(self.user)
        self.post_2 = Post.objects.create(
            author=self.user, content="my content1", title="my title2"
        )
        data = {"post": self.post_2.pk, "name": "name", "comment": "comment"}
        res = self.client.post(self.url, data=data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(len(Comment.objects.all()), 11)

class CommentDestroyTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email="example@gmail.com")
        self.post_1 = Post.objects.create(
            author=user, content="my content1", title="my title1"
        )
        self.post_comment = Comment.objects.create(
            post=self.post_1, name="my name", comment="my comment"
        )
    
    @property
    def url(self):
        return reverse("comment-destroy-api-view", kwargs={"pk": self.post_comment.pk})

    def test_delete(self):
        res = self.client.delete(self.url)
        self.assertEqual(res.status_code, 204)


class LikeListTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email="example@gmail.com")
        self.post = Post.objects.create(author=user, content="my content1", title="my title1")
        self.like = Like.objects.create(post=self.post, user=user)
    
    @property
    def url(self):
        return reverse('like-list-api-view', kwargs={"slug": self.post.slug})
    
    def test_get(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)

    def test_post(self):
        self.user = User.objects.get(email="example@gmail.com")
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user, content="my content1", title="my title2"
        )
        data = {"user": self.user.pk, "post": self.post.pk}
        res = self.client.post(self.url, data=data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(len(Like.objects.all()), 2)

class LikeDestroyTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email="example@gmail.com")
        self.post_1 = Post.objects.create(author=user, content="my content1", title="my title1")
        self.like_1 = Like.objects.create(post=self.post_1, user=user)
    
    @property
    def url(self):
        return reverse("like-destroy-api-view", kwargs={"pk": self.like_1.pk})

    def test_delete(self):
        res = self.client.delete(self.url)
        self.assertEqual(res.status_code, 204)
        self.assertEqual(len(Like.objects.all()), 0)
        

class CommentLikeListTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email="example@gmail.com")
        self.post_1 = Post.objects.create(
            author=user, content="my content1", title="my title1"
        )
        self.post_comment = Comment.objects.create(post=self.post_1, name="my name", comment="my comment")
        self.comment_like = CommentLike.objects.create(comment = self.post_comment, user=user)
    
    @property
    def url(self):
        return reverse('comment-like-list-api-view', kwargs ={"pk": self.post_comment.pk})

    def test_get(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)

    def test_post(self):
        self.user = User.objects.get(email="example@gmail.com")
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user, content="my content1", title="my title2"
        )
        self.comment = Comment.objects.create(
            post=self.post, name="my name", comment="my comment"
        )
        data = {"user": self.user.pk, "post": self.post.pk, "comment": self.comment.pk}
        res = self.client.post(self.url, data=data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(len(CommentLike.objects.all()), 2)
        
class CommentLikeDestroyTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email="example@gmail.com")
        self.post_1 = Post.objects.create(
            author=user, content="my content1", title="my title1"
        )
        self.post_comment = Comment.objects.create(post=self.post_1, name="my name", comment="my comment")
        self.comment_like = CommentLike.objects.create(comment = self.post_comment, user=user)

    @property
    def url(self):
        return reverse('comment-like-destroy-api-view', kwargs ={"pk": self.post_comment.pk})

    def test_delete(self):
        res = self.client.delete(self.url)
        self.assertEqual(res.status_code, 204)
        self.assertEqual(len(CommentLike.objects.all()), 0)