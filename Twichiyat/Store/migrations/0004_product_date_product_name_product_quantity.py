# Generated by Django 5.0 on 2023-12-29 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_remove_product_slugp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Anonymous Product', max_length=25),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
