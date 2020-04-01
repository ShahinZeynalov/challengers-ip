# Generated by Django 2.2.8 on 2020-04-01 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Applicant Statuses',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=1000)),
                ('sender_name', models.CharField(max_length=30)),
                ('sender_email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=200)),
                ('answer', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('motivation_letter', models.TextField(max_length=1000)),
                ('photo', models.FileField(blank=True, upload_to='static/applicant_photos')),
                ('status', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='ccapp.ApplicantStatus')),
            ],
        ),
    ]
