# Generated by Django 4.0.2 on 2022-03-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customers_rfc'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='actual_deb',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='max_credit',
            field=models.FloatField(blank=True, null=True),
        ),
    ]