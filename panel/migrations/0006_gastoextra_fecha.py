# Generated by Django 5.0.1 on 2024-02-25 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_gastoextra'),
    ]

    operations = [
        migrations.AddField(
            model_name='gastoextra',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]