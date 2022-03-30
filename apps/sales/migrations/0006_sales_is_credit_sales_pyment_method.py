# Generated by Django 4.0.2 on 2022-03-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_saledetails_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='is_credit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sales',
            name='pyment_method',
            field=models.TextField(blank=True, null=True),
        ),
    ]