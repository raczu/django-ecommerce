# Generated by Django 3.0.2 on 2020-04-20 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0018_auto_20200420_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 10, 48, 25, 936827)),
        ),
    ]