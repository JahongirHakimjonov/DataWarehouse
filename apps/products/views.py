from .serializers import (
    ProductSerializer,
    WarehouseSerializer,
    MaterialSerializer,
)
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Warehouse, ProductMaterial


class WarehouseViewSet(viewsets.ModelViewSet):
    serializer_class = WarehouseSerializer

    def get_queryset(self):
        # Omborxonadan kerakli xomashyolar
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
            product_materials = ProductMaterial.objects.filter(product=product)
            materials_data = []
            for product_material in product_materials:
                material_data = MaterialSerializer(product_material.material).data
                warehouses = Warehouse.objects.filter(
                    material=product_material.material
                ).order_by(
                    "id"
                )  # Order by id to use products in the order they were added
                total_qty = product_material.quantity * product.quantity
                for warehouse in warehouses:
                    if (
                        warehouse.remainder == 0
                    ):  # Skip the warehouse if its remainder is 0
                        continue
                    if total_qty <= 0:
                        break
                    if warehouse.remainder >= total_qty:
                        warehouse_temp_remainder = warehouse.remainder - total_qty
                        warehouse_data = WarehouseSerializer(warehouse).data
                        warehouse_data["warehouse_id"] = warehouse.id
                        warehouse_data["material_name"] = material_data["name"]
                        warehouse_data["qty"] = total_qty
                        warehouse_data["price"] = warehouse.price
                        total_qty = 0
                    else:
                        total_qty -= warehouse.remainder
                        warehouse_temp_remainder = 0
                        warehouse_data = WarehouseSerializer(warehouse).data
                        warehouse_data["warehouse_id"] = warehouse.id
                        warehouse_data["material_name"] = material_data["name"]
                        warehouse_data["qty"] = warehouse.remainder
                        warehouse_data["price"] = warehouse.price
                    materials_data.append(warehouse_data)

                if total_qty > 0:
                    materials_data.append(
                        {
                            "warehouse_id": None,
                            "material_name": material_data["name"],
                            "qty": total_qty,
                            "price": None,
                        }
                    )
            ordered_product_data = {
                "product_name": product.name,
                "product_qty": product.quantity,
                "product_materials": materials_data,
            }
            data.append(ordered_product_data)
        return Response({"result": data})
