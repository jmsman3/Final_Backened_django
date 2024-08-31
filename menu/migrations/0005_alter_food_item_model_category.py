# Generated by Django 5.0.6 on 2024-08-23 03:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_categorymodel_food_item_model_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_item_model',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='food_items', to='menu.categorymodel'),
        ),
    ]
