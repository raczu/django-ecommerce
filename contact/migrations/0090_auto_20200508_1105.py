# Generated by Django 3.0.2 on 2020-05-08 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0089_auto_20200506_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 11, 5, 15, 997745)),
        ),
    ]
