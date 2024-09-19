# Generated by Django 5.0 on 2024-01-01 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_order_note'),
        ('vendor_dashboard', '0004_alter_product_type_p'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(default='No comment', max_length=25),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_dashboard.product')),
            ],
        ),
    ]