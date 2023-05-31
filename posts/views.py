from django.shortcuts import render
from rest_framework.generics import ListAPIView
from posts.serializers import PostSerializer
from posts.models import Post

class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()