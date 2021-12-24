from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",
        "last_login",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
        "email",
        "groups",
        "user_permissions"]