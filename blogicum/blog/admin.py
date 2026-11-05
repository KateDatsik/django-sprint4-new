from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = ('title', 'slug', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
    )
    list_display_links = ('title',)
    list_editable = (
        'is_published',
        'category',
    )
    list_filter = ('is_published', 'category')
    search_fields = ('title',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
