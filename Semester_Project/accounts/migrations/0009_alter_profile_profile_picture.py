# Generated by Django 4.2 on 2023-04-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='user_placeholder.png', upload_to='static/images/profile_pictures'),
        ),
    ]
