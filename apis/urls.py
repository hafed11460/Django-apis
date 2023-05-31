from django.urls import path
from books.views import *

urlpatterns = [
    path('books/' , BookListAPIView.as_view(),name='books' )
]
