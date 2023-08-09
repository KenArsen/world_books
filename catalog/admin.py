from django.contrib import admin

from catalog import models


class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 0
    fields = ('book', 'inv_nom', 'imprint', 'status', 'due_back', 'borrower')


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    fields = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    fields = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    search_fields = ('first_name', 'last_name')
    ordering = ['date_of_birth']


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'genre')
    fields = ('title', 'genre', 'language', 'author', 'summary', 'isbn')
    list_filter = ('author', 'genre')
    search_fields = ('title',)
    inlines = [BookInstanceInline]


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    fields = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('inv_nom', 'book', 'borrower')
    list_display_links = ('book',)
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back', 'borrower')}),
    )
