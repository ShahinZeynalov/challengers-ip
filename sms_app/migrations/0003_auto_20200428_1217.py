# Generated by Django 2.2.8 on 2020-04-28 08:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0002_auto_20200427_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dairy',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 4, 28, 8, 17, 51, 547483, tzinfo=utc), verbose_name='Gün'),
        ),
        migrations.AlterField(
            model_name='notparticipating',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 4, 28, 8, 17, 51, 548942, tzinfo=utc), verbose_name='Day'),
        ),
    ]
