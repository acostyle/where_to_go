# Generated by Django 3.2.6 on 2021-09-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20210908_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение места'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='position',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='Позиция'),
        ),
    ]
