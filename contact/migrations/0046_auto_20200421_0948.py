# Generated by Django 3.0.2 on 2020-04-21 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0045_auto_20200421_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 9, 48, 55, 983658)),
        ),
    ]
