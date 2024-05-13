from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostListSerializers


# Create your views here.
@api_view(['GET'])
def index(request):
    posts = Post.objects.all()
    serializers = PostListSerializers(posts, many=True)
    return Response(serializers.data)