from django.shortcuts import render
from rest_framework.generics import ListAPIView
from books.models import Book
from books.serializers import BookSerializer
from books.permissions import IsAuthorOrReadOnly


class BookListAPIView(ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
