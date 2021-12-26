from rest_framework.generics import (DestroyAPIView, ListCreateAPIView,
                                     RetrieveAPIView)

from accounts.models import User
from accounts.serializers import UserSerializer


class UserListAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    def get_queryset(self, *args, **kwargs):
        return User.objects.all()

class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    def get_queryset(self, *args, **kwargs):
        return User.objects.all()