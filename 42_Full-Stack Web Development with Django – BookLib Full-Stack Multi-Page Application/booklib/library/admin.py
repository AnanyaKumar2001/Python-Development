from django.contrib import admin

from .models import Author, Book

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'release_year')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
