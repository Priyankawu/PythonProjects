# Generated by Django 3.1.5 on 2021-02-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210201_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]