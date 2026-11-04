from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'description']
    search_fields = ['slug', 'title', 'description']
    list_filter = ['slug', 'title']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'text', 'pub_date', 'author', 'location', 'category'
    ]
    search_fields = [
        'title', 'text', 'pub_date', 'author', 'location', 'category'
    ]
    list_filter = ['pub_date', 'author', 'category', 'location']
