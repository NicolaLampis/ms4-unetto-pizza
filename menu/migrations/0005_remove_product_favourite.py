# Generated by Django 3.2.7 on 2021-09-28 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_product_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='favourite',
        ),
    ]
