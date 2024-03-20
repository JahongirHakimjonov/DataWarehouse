from django.contrib import admin
from django.contrib.admin import register
from .models import Product, Material, ProductMaterial, Warehouse


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity"]
    search_fields = ["name"]
    list_filter = ["name"]


@register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]


@register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ["product", "material", "quantity"]
    search_fields = ["product", "material"]
    list_filter = ["product", "material"]


@register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["material", "remainder", "price"]
    search_fields = ["material", "remainder", "price"]
    list_filter = ["material", "remainder", "price"]

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('id')
