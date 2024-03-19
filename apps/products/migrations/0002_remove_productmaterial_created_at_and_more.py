# Generated by Django 5.0.3 on 2024-03-19 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productmaterial",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="productmaterial",
            name="updated_at",
        ),
        migrations.AlterField(
            model_name="productmaterial",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_materials",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="productmaterial",
            name="quantity",
            field=models.IntegerField(),
        ),
    ]
