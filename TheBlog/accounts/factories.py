import factory
from factory import faker


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.User"
    username = factory.Sequence(lambda n: 'User{0}'.format(n))
    email = factory.LazyAttribute(lambda obj: "%s@example.com" % obj.username)
    