from apps.shared.models import AbstractModel

from django.db import models


# Mahsulotlar uchun model
class Product(AbstractModel):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "products"


# Materiallar uchun model
class Material(AbstractModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"
        db_table = "materials"


# Mahsulot va materiallar uchun model
class ProductMaterial(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_materials"
    )
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.product.name} - {self.material.name}"

    class Meta:
        verbose_name = "Product Material"
        verbose_name_plural = "Product Materials"
        db_table = "product_materials"


# Omborxona uchun model
class Warehouse(AbstractModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.material.name} - {self.remainder}"

    class Meta:
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"
        db_table = "warehouses"
