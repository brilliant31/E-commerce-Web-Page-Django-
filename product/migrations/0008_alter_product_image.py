# Generated by Django 4.0.3 on 2022-10-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product/image'),
        ),
    ]
