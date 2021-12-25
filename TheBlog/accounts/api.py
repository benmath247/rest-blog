from accounts.serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from accounts.models import User

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