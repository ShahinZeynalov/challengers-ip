# Generated by Django 2.2.8 on 2020-04-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0003_delete_test'),
        ('sms_app', '0011_remove_dairy_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='badges',
            field=models.ManyToManyField(related_name='badge', to='dashboard_app.Badge'),
        ),
    ]
