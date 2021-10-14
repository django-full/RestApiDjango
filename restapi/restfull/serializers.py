from rest_framework import serializers
from .models import Post


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name','penulis']
