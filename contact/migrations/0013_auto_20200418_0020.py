# Generated by Django 3.0.2 on 2020-04-17 22:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0012_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 0, 20, 40, 484028)),
        ),
    ]
