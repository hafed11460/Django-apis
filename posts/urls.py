from django.urls import path
from posts.views import *

urlpatterns = [
    path('' , PostListAPIView.as_view(),name='posts' )
]
