# Generated by Django 3.2.6 on 2021-08-27 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placeimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='placeimage',
            name='position',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_images', to='places.place', verbose_name='Место'),
        ),
    ]
