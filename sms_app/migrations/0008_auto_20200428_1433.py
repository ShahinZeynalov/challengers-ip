# Generated by Django 2.2.8 on 2020-04-28 10:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0007_auto_20200428_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dairy',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 4, 28, 10, 33, 34, 805237, tzinfo=utc), verbose_name='Gün'),
        ),
        migrations.AlterField(
            model_name='notparticipating',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 4, 28, 10, 33, 34, 806650, tzinfo=utc), verbose_name='Day'),
        ),
    ]
