from rest_framework.serializers import ModelSerializer
from books.models import Book
from users.serializers import UserSerializer


class BookSerializer(ModelSerializer):
    authors = UserSerializer(many=True,read_only=True) 
    owner = UserSerializer()
    class Meta:
        model = Book
        fields = ['id','owner','title','price','publisher','pubdate','authors']