from django.test import TestCase
from rest_framework.test import APITestCase
from books.models import Book ,Publisher
from django.urls import reverse
from rest_framework import status
from users.models import User


# class APITests(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         publisher = Publisher('Eltaqwa')
#         p = publisher.save()
#         cls.book = Book.objects.create(
#             title = 'Django for Apis',
#             price = 1500,
#             publisher =p ,
#             # authors = User.objects.all()[:2],
#             pubdate ='2023-05-30'
#         )
    
#     def test_api_listview(self):
#         response  = self.client.get(reverse('books'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Book.objects.count(), 1)
#         self.assertContains(response, self.book)