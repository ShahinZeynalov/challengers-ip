# Generated by Django 2.2.8 on 2020-04-30 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0008_auto_20200421_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='badges',
        ),
    ]
