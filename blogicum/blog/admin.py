from django.contrib import admin
from .models import Category, Location, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    search_fields = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'location',
        'is_published',
        'pub_date',
    )
    search_fields = ('title', 'text')
    list_filter = (
        'is_published',
        'category',
        'location',
    )
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)
    autocomplete_fields = (
        'category',
        'location',
    )
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'title',
                    'text',
                    'author',
                    'category',
                    'location',
                    'image',
                ),
            },
        ),
        (
            'Публикация',
            {
                'fields': (
                    'pub_date',
                    'is_published',
                ),
            },
        ),
        (
            'Служебное',
            {
                'fields': ('created_at',),
                'classes': ('collapse',),
            },
        ),
    )
    readonly_fields = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')


# Localize admin site titles to Russian
admin.site.site_header = 'Панель администратора'
admin.site.site_title = 'Администрирование'
admin.site.index_title = 'Добро пожаловать в админ-зону'
