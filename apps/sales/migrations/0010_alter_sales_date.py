# Generated by Django 4.0.2 on 2022-03-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_alter_sales_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
