# Generated by Django 3.0.2 on 2020-04-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200423_1634'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
