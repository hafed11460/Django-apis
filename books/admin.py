from django.contrib import admin
from books.models import Book, Store, Publisher


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id','name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['owner','title', 'price', 'publisher','pubdate']


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Publisher , PublisherAdmin)
admin.site.register(Book , BookAdmin)
admin.site.register(Store , StoreAdmin)
