from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            firstname='testuser',
            lastname='testuser',
            email="test@gmail.com",
            password = 'Azerty@123'
        )
        cls.post = Post.objects.create(
            title='New for django developers',
            body='this is a new information for django developers',
            author = cls.user
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.author.firstname,'testuser')
        self.assertEqual(self.post.author.lastname,'testuser')
        self.assertEqual(self.post.title,'New for django developers')
        self.assertEqual(self.post.body,'this is a new information for django developers')
        self.assertEqual(str(self.post),'New for django developers')
