# Generated by Django 3.1.2 on 2020-11-23 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201123_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_shelf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.shelf'),
        ),
    ]