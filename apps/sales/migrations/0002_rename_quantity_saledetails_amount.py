# Generated by Django 4.0.2 on 2022-03-10 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saledetails',
            old_name='quantity',
            new_name='amount',
        ),
    ]
