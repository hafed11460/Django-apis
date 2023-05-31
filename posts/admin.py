from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'body', 'author','created_at','updated_at']
    list_display_links =['title']    


admin.site.register(Post, PostAdmin)