# Generated by Django 4.0.4 on 2022-06-12 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_category_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='manufacturer',
            new_name='manufacturer_id',
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='category',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='product',
            new_name='product_id',
        ),
    ]
