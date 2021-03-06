from rest_framework import serializers

from blog.models import Comment, CommentLike, Like, Post, PostReaction

all = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = all


class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()


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


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = all
