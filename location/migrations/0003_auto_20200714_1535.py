# Generated by Django 3.0.8 on 2020-07-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20200709_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observationpost',
            name='obs_lat',
            field=models.DecimalField(decimal_places=10, max_digits=999),
        ),
        migrations.AlterField(
            model_name='observationpost',
            name='obs_lon',
            field=models.DecimalField(decimal_places=10, max_digits=999),
        ),
    ]
