# Generated by Django 3.0.2 on 2020-04-20 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_auto_20200418_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 9, 46, 47, 848444)),
        ),
    ]
