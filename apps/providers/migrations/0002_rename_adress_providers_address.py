# Generated by Django 4.0.2 on 2022-03-10 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='providers',
            old_name='adress',
            new_name='address',
        ),
    ]
