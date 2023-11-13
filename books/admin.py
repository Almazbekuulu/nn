from django.contrib import admin



from django.contrib import admin
from .models import Author, Genre, Publisher, Book, Reader

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'page_count', 'isbn')
    list_filter = ('author', 'publication_date')
    search_fields = ('title', 'author__name', 'isbn')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'country')
    search_fields = ('name', 'country')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    search_fields = ('name',)

class ReaderAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_email', 'user_first_name', 'user_last_name')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')

    def user_email(self, obj):
        return obj.user.email

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
