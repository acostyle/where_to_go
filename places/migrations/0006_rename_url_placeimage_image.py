# Generated by Django 3.2.6 on 2021-09-01 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20210828_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placeimage',
            old_name='url',
            new_name='image',
        ),
    ]
