# Generated by Django 4.0.2 on 2022-03-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='products/generic/131-1312918_png-file-svg-product-icon-transparent-png.png', max_length=255, null=True, upload_to='profiles/'),
        ),
    ]
