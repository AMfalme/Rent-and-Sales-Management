# Generated by Django 3.1.2 on 2020-11-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
