# Generated by Django 3.1.2 on 2020-11-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201123_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='products/product1.jpg', upload_to=''),
        ),
    ]
