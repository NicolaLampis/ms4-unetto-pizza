from django.contrib import admin
from .models import Category, Product, Deal, Allergen


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
        'price',
        'favourite',
        'deal',
        'allergens',
    )


admin.site.register(Product, ProductAdmin)


class DealAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Deal, DealAdmin)


class AllergenAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'data_url',
    )


admin.site.register(Allergen, AllergenAdmin)
