from rest_framework import serializers
from .models import Post

class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'category',)