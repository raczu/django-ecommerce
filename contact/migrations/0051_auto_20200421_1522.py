# Generated by Django 3.0.2 on 2020-04-21 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0050_auto_20200421_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 15, 22, 45, 559939)),
        ),
    ]
