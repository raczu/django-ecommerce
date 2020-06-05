# Generated by Django 3.0.2 on 2020-05-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200503_2142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variation',
            options={'ordering': ['product']},
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('size', 'size'), ('universal', 'universal')], default='universal', max_length=120),
        ),
    ]