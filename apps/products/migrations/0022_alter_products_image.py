# Generated by Django 4.0.2 on 2022-05-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_products_in_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='products/generic/img_566093.png', max_length=255, null=True, upload_to='profiles/'),
        ),
    ]
