# Generated by Django 4.0.2 on 2022-03-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='profiles/generic/profile_happy.png', max_length=255, null=True, upload_to='profiles/'),
        ),
    ]
