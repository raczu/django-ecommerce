# Generated by Django 3.0.2 on 2020-05-06 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0086_auto_20200504_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 15, 38, 29, 798858)),
        ),
    ]
