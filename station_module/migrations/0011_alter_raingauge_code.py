# Generated by Django 5.0.1 on 2024-01-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station_module', '0010_alter_raingauge_last_rainfall_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raingauge',
            name='code',
            field=models.IntegerField(unique=True, verbose_name='کد'),
        ),
    ]
