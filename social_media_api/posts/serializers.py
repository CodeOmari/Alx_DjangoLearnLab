from rest_framework import serializers
from .models import Post, Comment
from django.conf import settings
from accounts.serializers import CustomUserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL  # Use the custom user model
        fields = ['id', 'username']



class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'id']

    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(author=user, **validated_data)



class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(author=user, **validated_data)