# Generated by Django 3.0.2 on 2020-05-04 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0085_auto_20200504_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 14, 38, 47, 775374)),
        ),
    ]
