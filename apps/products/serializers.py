from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouse


# Omborxona ma'lumotlarini serializatsiya qilish uchun klass
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["price"]


# Mahsulot materiallarini serializatsiya qilish uchun klass
class ProductMaterialSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(many=True, read_only=True)

    class Meta:
        model = ProductMaterial
        fields = ["material", "quantity", "warehouse"]


# Mahsulotlarni serializatsiya qilish uchun klass
class ProductSerializer(serializers.ModelSerializer):
    product_materials = ProductMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["product_materials"]


# Materiallarni serializatsiya qilish uchun klass
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ["name"]
