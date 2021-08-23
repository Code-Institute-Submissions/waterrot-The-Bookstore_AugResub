from django.contrib import admin
from .models import Product, Category, Author, Release


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_of_birth',
        'books',
    )


class ReleaseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'new',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Release, ReleaseAdmin)
