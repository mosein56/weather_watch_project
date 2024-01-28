# Generated by Django 5.0.1 on 2024-01-24 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station_module', '0011_alter_raingauge_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='parent_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='station_module.station', verbose_name='ایستگاه والد'),
        ),
        migrations.AlterField(
            model_name='station',
            name='code',
            field=models.IntegerField(max_length=5, unique=True, verbose_name='کد'),
        ),
    ]
