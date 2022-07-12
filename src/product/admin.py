from django.contrib import admin
from .models import Variant, Product, ProductImage, ProductVariant, ProductVariantPrice


# Register your models here.

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    model = Variant
    list_display = (
        'title', 'active', 'created_at', 'updated_at'
    )
    ordering = ('-created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        'title', 'sku', 'created_at', 'updated_at'
    )
    ordering = ('-created_at',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    model = ProductImage
    list_display = (
        'product', 'file_path', 'created_at', 'updated_at'
    )
    ordering = ('-created_at',)


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    model = ProductVariant
    list_display = (
        'variant_title', 'variant', 'product', 'created_at', 'updated_at'
    )
    ordering = ('-created_at',)


@admin.register(ProductVariantPrice)
class ProductVariantPriceAdmin(admin.ModelAdmin):
    model = ProductVariantPrice
    list_display = (
        'product',
        'product_variant_one',
        'product_variant_two',
        'product_variant_three',
        'price', 'stock', 'created_at', 'updated_at'
    )
    ordering = ('-created_at',)
