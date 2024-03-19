from .serializers import (
    ProductSerializer,
    WarehouseSerializer,
    MaterialSerializer,
)
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Warehouse, ProductMaterial, Material


class WarehouseViewSet(viewsets.ModelViewSet):
    serializer_class = WarehouseSerializer

    def get_queryset(self):
        product_materials = ProductMaterial.objects.filter(
            product__name=self.request.query_params.get("product_name")
        )
        material_ids = product_materials.values_list("material", flat=True)
        return Warehouse.objects.filter(material__in=material_ids)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for product in queryset:
            product_data = ProductSerializer(product).data
            product_materials = ProductMaterial.objects.filter(product=product)
            materials_data = []
            for product_material in product_materials:
                material_data = MaterialSerializer(product_material.material).data
                warehouses = Warehouse.objects.filter(
                    material=product_material.material
                )
                for warehouse in warehouses:
                    warehouse_data = WarehouseSerializer(warehouse).data
                    warehouse_data["warehouse_id"] = warehouse.id
                    warehouse_data["material_name"] = material_data["name"]
                    warehouse_data["qty"] = product_material.quantity
                    warehouse_data["price"] = warehouse.price
                    materials_data.append(warehouse_data)
            # Create a new dictionary and add the keys in the desired order
            ordered_product_data = {
                "product_name": product.name,
                "product_qty": product.quantity,
                "product_materials": materials_data,
            }
            data.append(ordered_product_data)
        return Response({"result": data})
