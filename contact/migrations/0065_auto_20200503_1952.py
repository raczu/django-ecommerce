# Generated by Django 3.0.2 on 2020-05-03 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0064_auto_20200502_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 19, 52, 31, 407436)),
        ),
    ]
