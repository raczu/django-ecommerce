# Generated by Django 3.0.2 on 2020-04-21 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0049_auto_20200421_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 15, 21, 43, 577844)),
        ),
    ]