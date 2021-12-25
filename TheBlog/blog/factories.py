import factory

from accounts.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Post'

    title = factory.Sequence(lambda n: f'Post Title {n}')
    content = factory.Faker('text')

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Comment'
    comment = factory.Faker('text')

class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Like'

class CommentLikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.CommentLike'
