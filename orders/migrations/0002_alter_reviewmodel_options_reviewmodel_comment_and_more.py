# Generated by Django 5.0.6 on 2024-08-23 00:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_food_itme_special_offer_model_food_item'),
        ('orders', '0001_initial'),
        ('users', '0002_alter_profile_mobile_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewmodel',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='food_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.food_item_model'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='rating',
            field=models.CharField(blank=True, choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
