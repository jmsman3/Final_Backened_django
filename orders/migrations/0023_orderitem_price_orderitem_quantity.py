# Generated by Django 5.0.6 on 2024-08-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_remove_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
