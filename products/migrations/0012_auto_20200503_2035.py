# Generated by Django 3.0.2 on 2020-05-03 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200503_2024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VariationManager',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='category',
        ),
    ]