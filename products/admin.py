from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'avg_rating',
        'image',
    )

    ordering = ('sku',)
    readonly_fields = ('avg_rating',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'comment',
        'rate',
        'date_posted',
    )
    readonly_fields = (
        'date_posted',
    )


admin.site.register(Review)
