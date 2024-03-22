# Generated by Django 5.0.1 on 2024-02-20 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_venta_observaciones_venta_pagado'),
    ]

    operations = [
        migrations.CreateModel(
            name='GastoExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.producto')),
            ],
        ),
    ]
