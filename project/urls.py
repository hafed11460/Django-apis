
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/posts/', include('posts.urls')),
    path("api-auth/", include("rest_framework.urls"))
]
