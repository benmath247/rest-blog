import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.User"

    email = factory.LazyAttribute(lambda obj: "%s@example.com" % obj.username)
