# Generated by Django 4.0.2 on 2022-03-24 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='products/generic/img_566093.png', max_length=255, null=True, upload_to='profiles/'),
        ),
    ]
