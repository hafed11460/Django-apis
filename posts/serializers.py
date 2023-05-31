from posts.models import Post
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer


class PostSerializer(ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title','body','author','created_at','deleted_at']