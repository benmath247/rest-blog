from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%s' % (self.username)