# Generated by Django 2.2.8 on 2020-04-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0002_auto_20200401_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='user/images'),
        ),
    ]