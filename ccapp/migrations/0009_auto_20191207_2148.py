# Generated by Django 2.2.6 on 2019-12-07 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0008_auto_20191207_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='ccapp.ApplicantStatus'),
        ),
    ]