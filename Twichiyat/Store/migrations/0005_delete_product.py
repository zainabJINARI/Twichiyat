# Generated by Django 5.0 on 2023-12-29 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_product_date_product_name_product_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
