# Generated by Django 3.2.16 on 2023-12-11 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20231209_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 15, 54, 34, 401652), verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 15, 54, 34, 401652), verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 15, 54, 34, 401652), verbose_name='Добавлено'),
        ),
    ]
