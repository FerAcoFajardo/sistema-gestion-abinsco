# Generated by Django 4.0.2 on 2022-03-10 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('credits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='customers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers'),
        ),
    ]