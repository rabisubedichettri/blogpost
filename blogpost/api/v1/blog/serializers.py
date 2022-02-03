from rest_framework import serializers
from blog.models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'user', "Description", 'published_at', 'active', 'slug']
        read_only_fields = ['id']  # can not be editable
