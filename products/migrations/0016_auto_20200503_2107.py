# Generated by Django 3.0.2 on 2020-05-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200503_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='varcategory',
            new_name='variation_category',
        ),
    ]
