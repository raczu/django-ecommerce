# Generated by Django 3.0.2 on 2020-05-03 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0068_auto_20200503_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 20, 24, 33, 477143)),
        ),
    ]
