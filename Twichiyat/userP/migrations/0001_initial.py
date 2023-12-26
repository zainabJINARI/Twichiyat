# Generated by Django 5.0 on 2023-12-26 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vendor', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=150)),
                ('phone_nbr', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Women', 'Women'), ('Men', 'Men')], default='Women', max_length=50)),
                ('slugU', models.SlugField(default=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
