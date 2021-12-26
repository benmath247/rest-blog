from django.shortcuts import reverse
from django.test import TestCase
from rest_framework.test import APITestCase

from accounts.factories import UserFactory
from accounts.models import User


# Create your tests here.
class UserListTestCase(APITestCase):
    def setUp(self):
        user1 = UserFactory()
        user2 = UserFactory()
        user3 = UserFactory()

    @property
    def url(self):
        return reverse('user-list-api-view')

    def test_get(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(User.objects.all()), 3)

class UserDestroyTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()

    @property
    def url(self):
        return reverse('user-destroy-api-view', kwargs={"pk": self.user.pk})

    def test_delete(self):
        res = self.client.delete(self.url)
        self.assertEqual(res.status_code, 204)
        self.assertEqual(len(User.objects.all()), 0)

class UserRetrieveAPIView(APITestCase):
    def setUp(self):
        self.user = UserFactory()
    
    @property
    def url(self):
        return reverse('user-retrieve-api-view', kwargs={"pk": self.user.pk})

    def test_get(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(User.objects.all()), 1)
        self.assertEqual(res.json()['id'], 1)

