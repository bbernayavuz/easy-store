# Generated by Django 4.0.4 on 2022-06-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]