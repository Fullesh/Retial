# Generated by Django 5.0.7 on 2024-07-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0004_alter_network_debt_alter_network_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание продукта'),
        ),
    ]