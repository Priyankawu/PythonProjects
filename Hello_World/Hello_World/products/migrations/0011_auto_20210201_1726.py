# Generated by Django 3.1.5 on 2021-02-02 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210201_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('treats', 'treats')], max_length=60),
        ),
    ]
