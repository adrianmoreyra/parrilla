# Generated by Django 5.0.1 on 2024-02-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_remove_producto_precio_producto_precio_compra_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='pagado',
            field=models.BooleanField(default=True),
        ),
    ]
