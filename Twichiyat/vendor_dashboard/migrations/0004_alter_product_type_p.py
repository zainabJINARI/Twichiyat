# Generated by Django 5.0 on 2023-12-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_dashboard', '0003_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_p',
            field=models.CharField(max_length=25),
        ),
    ]
