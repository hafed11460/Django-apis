from django.urls import path
from books.views import *

urlpatterns = [
    path('' , BookListAPIView.as_view(),name='books' )
]
