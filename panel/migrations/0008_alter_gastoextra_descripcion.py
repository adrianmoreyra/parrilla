# Generated by Django 5.0.1 on 2024-03-09 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_gastoextra_descripcion_alter_gastoextra_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoextra',
            name='descripcion',
            field=models.TextField(blank=True, default='   '),
        ),
    ]
