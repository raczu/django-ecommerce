# Generated by Django 3.0.2 on 2020-04-17 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_auto_20200417_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
