# Generated by Django 4.2.6 on 2024-01-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_alter_sitebanner_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitebanner',
            name='position',
            field=models.CharField(choices=[('station_list', 'لیست ایستگاهها'), ('station_detail', 'جزئیات ایستگاه'), ('about_us', 'درباره ما'), ('article_list', 'مقالات')], max_length=200, verbose_name='جایگاه نمایشی'),
        ),
    ]
