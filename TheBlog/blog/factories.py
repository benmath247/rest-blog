import factory

import blog.models

from accounts.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "blog.Post"

    title = factory.Sequence(lambda n: f"Post Title {n}")
    content = factory.Faker("text")
    image = factory.django.ImageField(width=1024, height=768)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "blog.Comment"

    comment = factory.Faker("text")
    name = factory.Faker("name")
    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)


class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "blog.Like"

    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)


class CommentLikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "blog.CommentLike"

    user = factory.SubFactory(UserFactory)
    comment = factory.SubFactory(CommentFactory)



class ReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "blog.PostReaction"

    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)
    reaction = factory.Faker('random_choices', elements=blog.models.PostReaction.CHOICES)
