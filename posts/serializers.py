from posts.models import Post
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'id','title','body','author','created_at','updated_at']


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ['updated_at','created_at',]
        fields = [ 'title','body','author','updated_at','created_at',]
        