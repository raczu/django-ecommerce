# Generated by Django 3.0.2 on 2020-04-21 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0038_auto_20200421_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 9, 38, 24, 811558)),
        ),
    ]
