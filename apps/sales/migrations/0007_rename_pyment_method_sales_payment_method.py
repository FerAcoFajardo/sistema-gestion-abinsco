# Generated by Django 4.0.2 on 2022-03-30 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_sales_is_credit_sales_pyment_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='pyment_method',
            new_name='payment_method',
        ),
    ]
