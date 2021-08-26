# Generated by Django 3.2.6 on 2021-08-26 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='place_images', verbose_name='Изображение места')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='places.place', verbose_name='Место')),
            ],
        ),
    ]
