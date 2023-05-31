from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from posts.serializers import PostSerializer,PostCreateSerializer
from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly


class PostListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()