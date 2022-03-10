# Generated by Django 4.0.2 on 2022-03-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=13)),
                ('adress', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'providers',
                'verbose_name_plural': 'providers',
                'db_table': 'providers',
                'ordering': ['id'],
            },
        ),
    ]