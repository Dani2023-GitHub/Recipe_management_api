# Generated by Django 5.1.3 on 2025-01-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile_image.jpg', upload_to='profile_image'),
        ),
    ]
