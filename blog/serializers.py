from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User # Import User for the author field

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'post_id',
            'url',          
            'title',
            'source',
            'description',
            'published_at',
            'story',
            'type',
            'author',
            'hero'
        ]
        read_only_fields = ['post_id', 'published_at']