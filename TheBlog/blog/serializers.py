from rest_framework import serializers
from blog.models import Comment, CommentLike, Post, Like

all = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = all

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = all

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = all

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = all