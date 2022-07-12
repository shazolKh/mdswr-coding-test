# Generated by Django 4.0.6 on 2022-07-12 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productvariant_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant_product', related_query_name='variant_product', to='product.variant'),
        ),
        migrations.AlterField(
            model_name='productvariantprice',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_price_Product', related_query_name='product_variant_price', to='product.product'),
        ),
    ]