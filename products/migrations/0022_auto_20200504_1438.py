# Generated by Django 3.0.2 on 2020-05-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20200504_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('size', 'size'), ('shoe_size', 'shoe_size')], default='universal', max_length=120),
        ),
    ]
