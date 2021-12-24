import factory

from accounts.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Post'

    title = factory.Sequence(lambda n: f'Post Title {n}')
    author = UserFactory()
    content = factory.Faker('text')
